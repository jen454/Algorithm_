# -*- coding: utf-8 -*-
"""
generate_post.py

사용법:
    python generate_post.py <문제_폴더_경로> [--platform leetcode|programmers|baekjoon]

예시:
    python generate_post.py ../problems/0383-ransom-note
    python generate_post.py ../problems/프로그래머스/42862-체육복 --platform programmers

동작:
    1. 폴더 안에서 solution.* (py, java, js, cpp 등) 파일을 찾는다.
    2. 같은 폴더에 README.md(문제 설명, leetcode-sync verbose 모드 또는 수동 작성)가 있으면 같이 읽는다.
    3. Claude Code CLI(claude -p, headless 모드)를 호출한다:
       - 코드 안의 주석(접근방식/풀이 로직이 담겨 있다고 가정)을 근거로 접근방식/풀이 서술
       - README의 문제 설명/제약조건으로 맥락 보강
       - 고정된 블로그 형식(문제 접근 / 풀이 / 전체 코드)으로 마크다운 생성
    4. posts/ 폴더에 결과를 저장한다.

    * note.md는 더 이상 필요하지 않다. 접근방식/풀이는 코드 주석에서 추출한다.
      단, 레거시 note.md가 폴더에 남아있으면 참고 자료로 추가 활용한다.

인증 (API 키가 아닌 Claude 구독을 사용):
    1. 로컬에서 `claude setup-token` 실행 -> Pro/Max 구독으로 OAuth 로그인 -> 장기 토큰 발급
    2. 발급된 토큰을 환경변수 CLAUDE_CODE_OAUTH_TOKEN 으로 설정
       (GitHub Actions에서는 리포지토리 시크릿으로 등록)
    3. ANTHROPIC_API_KEY는 설정하지 않는다 (설정돼 있으면 그쪽이 우선되어 종량 과금됨)

요구사항:
    - Claude Code CLI가 설치되어 있어야 한다: npm install -g @anthropic-ai/claude-code
"""

from __future__ import annotations

import os
import re
import sys
import json
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# 설정
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
POSTS_DIR = REPO_ROOT / "posts"

# solution 코드로 인정할 확장자 우선순위
SOLUTION_EXTENSIONS = [".py", ".java", ".js", ".ts", ".cpp", ".c", ".go"]

MODEL = "claude-sonnet-5"
CLAUDE_TIMEOUT_SECONDS = 180

# ---------------------------------------------------------------------------
# 플랫폼 판별 (경로 패턴 기반)
# ---------------------------------------------------------------------------

def detect_platform(problem_dir: Path, override: str | None) -> str:
    if override:
        return override

    path_str = str(problem_dir)

    if "프로그래머스" in path_str:
        return "programmers"
    if "백준" in path_str:
        return "baekjoon"

    # destination-folder: leetcode 설정 이후 -> leetcode/ 하위 폴더로 들어옴
    if re.search(r"(^|/)leetcode(/|$)", path_str):
        return "leetcode"

    # (레거시) destination-folder 설정 전: 루트 바로 아래 "숫자-문제명" 폴더 패턴
    folder_name = problem_dir.name
    if re.match(r"^\d{3,5}-", folder_name):
        return "leetcode"

    return "unknown"


PLATFORM_LABEL = {
    "leetcode": "LeetCode",
    "programmers": "프로그래머스",
    "baekjoon": "백준",
    "unknown": "알 수 없음",
}


# ---------------------------------------------------------------------------
# 파일 찾기
# ---------------------------------------------------------------------------

def find_solution_file(problem_dir: Path) -> Path | None:
    for ext in SOLUTION_EXTENSIONS:
        candidates = list(problem_dir.glob(f"*{ext}"))
        # note.md, README 등은 제외하고 solution 계열 파일만
        candidates = [c for c in candidates if "solution" in c.stem.lower() or len(candidates) == 1]
        if candidates:
            return candidates[0]
    # fallback: 확장자 상관없이 solution이 이름에 들어간 파일
    for f in problem_dir.iterdir():
        if f.is_file() and "solution" in f.stem.lower():
            return f
    return None


def find_readme_file(problem_dir: Path) -> Path | None:
    for name in ("README.md", "readme.md", "Readme.md"):
        p = problem_dir / name
        if p.exists():
            return p
    return None


# LeetHub가 루트 README.md에 쌓는 토픽 이름 -> 블로그 해시태그용 한글 표기.
# 여기에 없는 토픽은 Claude가 문맥에 맞게 옮긴다.
TOPIC_KO = {
    "Array": "배열",
    "String": "문자열",
    "Hash Table": "해시맵",
    "Math": "수학",
    "Stack": "스택",
    "Queue": "큐",
    "Two Pointers": "투포인터",
    "Binary Search": "이진탐색",
    "Sorting": "정렬",
    "Greedy": "그리디",
    "Dynamic Programming": "다이나믹프로그래밍",
    "Recursion": "재귀",
    "Simulation": "시뮬레이션",
    "Prefix Sum": "누적합",
    "Matrix": "행렬",
    "Counting": "카운팅",
    "Sliding Window": "슬라이딩윈도우",
    "Linked List": "연결리스트",
    "Tree": "트리",
    "Binary Tree": "이진트리",
    "Graph": "그래프",
    "Depth-First Search": "DFS",
    "Breadth-First Search": "BFS",
    "Heap (Priority Queue)": "힙",
    "Bit Manipulation": "비트연산",
    "Backtracking": "백트래킹",
}


def extract_leetcode_topics(problem_dir_name: str) -> list[str]:
    """루트 README.md의 "LeetCode Topics" 표에서 이 문제가 속한 토픽들을 뽑는다.

    LeetHub는 루트 README.md에 "## <토픽>" 섹션별 표를 누적으로 쌓고,
    각 행에 "[<문제 폴더명>](링크)" 형태로 문제를 넣는다.
    따라서 문제 폴더명이 들어있는 행의 상위 "## 토픽"을 모으면 된다.
    """
    readme = REPO_ROOT / "README.md"
    if not readme.exists():
        return []

    topics: list[str] = []
    current: str | None = None
    for line in readme.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1)
            continue
        if current and f"[{problem_dir_name}]" in line and current not in topics:
            topics.append(current)
    return topics


def find_note_file(problem_dir: Path) -> Path | None:
    """레거시 지원: note.md가 남아있으면 참고 자료로 추가 사용."""
    note_path = problem_dir / "note.md"
    return note_path if note_path.exists() else None


# ---------------------------------------------------------------------------
# 프롬프트 구성
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """당신은 알고리즘 문제 풀이를 기술 블로그 글로 정리해주는 어시스턴트입니다.
아래 고정된 형식을 반드시 그대로 따라야 합니다. 형식을 벗어나거나 섹션을 추가/삭제하지 마세요.

출력 형식:

# [{platform}] {problem_title} ({language_display} 풀이)

## 문제접근
{problem_url}

(문제 설명과 접근 방법을 자연스러운 설명체로 서술. 불릿(-)이나 "문제 링크:" 같은 라벨 없이, 링크 다음 줄부터 바로 이어서 씁니다. 아래 "줄바꿈 규칙"대로 문장마다 빈 줄로 나누어 씁니다.)
- 코드 주석에서 여러 개의 판단/고민 지점이 드러나면(예: "A 방식을 생각했지만 B가 나을 것 같다", 예외 케이스 처리, 두 가지 중 뭘 쓸지 고민 등), 각각을 **"번호. 질문형 소제목"** 형태의 볼드로 나누어 서술하세요. 예: **1. reserve 순회 vs 전체 배열 활용, 뭘 써야 하지?**
  - 각 볼드 소제목 아래에 실제 고민한 내용을 문단으로 풀어 쓰고, 결론이 있다면 `**-> 결론 내용**` 처럼 화살표+볼드로 강조하세요.
  - 판단/고민 지점이 명확히 하나뿐이거나 단순한 문제라면 억지로 여러 개로 쪼개지 말고, 자연스러운 설명 문단으로 서술하세요.

## 풀이
번호가 필요한 단계별 설명은 **볼드 번호**로 구분하세요 (예: `**1.** arr1은 nums[0]으로 초기화한다.`). 각 단계는 "~한다" 체로, 접근 방법에서 정리한 논리를 실제 코드 흐름에 맞춰 순서대로 풀어 쓰세요.

## 전체코드
```{language}
(코드 로직/구조는 원본 그대로 유지하되, 풀이 설명이 될 만한 주석은 추가하거나 보강해도 됩니다.
 단, 작성자가 접근방식을 정리해둔 메모 성격의 주석 블록은 여기에 옮기지 마세요.)
```

#태그1 #태그2
(마지막 줄은 위 예시처럼 `#`으로 시작하는 태그 2~3개를 공백으로 구분해 한 줄로만 씁니다. "추천 태그:" 같은 접두사나 라벨, 헤더, 불릿은 절대 붙이지 마세요. 줄 전체가 `#`으로 시작해야 합니다. 태그를 고를 때는 아래 "LeetCode 토픽"이 주어졌다면 그것을 1순위 후보로 삼되, **코드에 실제로 쓰인 것만** 고르세요. LeetCode 토픽에는 이 풀이가 쓰지 않은 다른 접근법(예: 배열로 푼 문제에 붙은 "Trie", "Dynamic Programming")도 섞여 있으므로 그대로 옮기지 말고 걸러내야 합니다. 토픽이 없거나 코드와 맞는 게 없으면 코드 로직에서 직접 판단하세요. 태그는 코드의 실제 로직에서 확인되는 알고리즘 개념/자료구조만 다세요. 예: 배열을 순회하며 조건 비교만 하면 "#배열" "#시뮬레이션", 두 포인터가 양 끝에서 좁혀오면 "#투포인터", 매 단계 최적을 선택해 전체 최적을 구성하면 "#그리디" 등. 코드에 실제로 쓰이지 않은 기법을 그럴듯해 보인다고 갖다 붙이지 마세요.)

중요한 규칙:
- 마크다운 헤더(`#`, `##`, `###`)는 위 세 섹션 제목("문제접근", "풀이", "전체코드")에만 사용하세요. 그 외에는 절대 헤더를 만들지 마세요 (소제목이 필요하면 볼드체를 사용). 단 맨 마지막 태그 줄은 헤더가 아니라 해시태그이므로 `#태그1 #태그2` 형태 그대로 씁니다.
- 문서의 맨 마지막 줄은 반드시 해시태그 줄이어야 하며, 그 뒤에 마무리 문장이나 설명을 덧붙이지 마세요.
- 각 섹션(문제접근/풀이/전체코드) 헤더 앞에는 빈 줄을 두 개 넣어서 섹션 사이에 여백을 주세요.
- **줄바꿈 규칙(매우 중요)**: 마침표로 문장이 끝날 때마다 줄을 바꾸고, 문장과 문장 사이에는 반드시 **빈 줄을 한 개** 넣으세요. 한 줄에 여러 문장을 이어 쓰지 마세요.
  - 개행 문자 하나만 넣는 것으로는 부족합니다. 티스토리 등 마크다운 뷰어는 빈 줄이 없는 줄바꿈을 무시하고 앞 문장에 그대로 이어 붙이기 때문에, 빈 줄이 없으면 문단이 한 덩어리로 뭉쳐 보입니다.
  - 이 규칙은 "문제접근"과 "풀이" 섹션의 모든 설명 문장, 볼드 번호 항목(`**1.** ...`), 볼드 소제목, `**-> 결론**` 줄에 똑같이 적용됩니다. 각 항목 사이에도 빈 줄을 넣으세요.
  - 코드블록(```` ``` ```` 안쪽) 내부에는 이 규칙을 적용하지 마세요. 코드는 원본 형태 그대로 둡니다.
- "문제접근" 섹션 첫 줄은 문제 링크만 단독으로 쓰고, 그 다음 줄부터 바로 설명 문단을 이어서 쓰세요. 불릿(-) 기호나 "문제 링크:" 같은 라벨을 붙이지 마세요.
- 제목에 문제 번호(예: "3069.")를 포함하지 마세요. 문제 이름만 사용하세요.
- 정보 출처는 두 가지입니다: (1) 코드 안의 주석 — 작성자가 직접 남긴 접근방식/풀이 로직, (2) README — 문제 설명/제약조건.
- "문제접근"과 "풀이" 섹션, 그리고 추천 태그의 내용은 반드시 코드 주석/코드 로직에 실제로 근거해야 합니다. 코드에 없는 사고 과정이나, 실제로 쓰이지 않은 알고리즘 기법(예: 투포인터, 그리디 등)을 그럴듯하다는 이유로 지어내지 마세요.
- 주석이 짧은 키워드나 단편적인 메모 수준이어도, 그 내용을 벗어나지 않는 선에서 자연스러운 설명체 문장으로 풀어써도 됩니다. 다만 주석에 없는 새로운 판단 근거나 비교를 창작하지는 마세요.
- 주석이 거의 없어서 접근방식을 알 수 없는 경우, 코드 구조 자체(변수명, 로직 흐름)에서 합리적으로 추론 가능한 범위까지만 서술하고, 과도하게 확신에 찬 어조로 추측하지 마세요.
- README(문제 설명)는 "문제접근" 섹션 도입부에서 문제가 무엇을 요구하는지 설명하는 데 사용하세요. 코드 주석과 결합해서 왜 그런 접근을 택했는지 자연스럽게 이어지도록 구성하세요.
- **접근 메모 주석은 전체코드에 넣지 마세요(중요)**: 작성자가 풀이 전에 생각을 정리해둔 메모성 주석(주로 파일 맨 위나 맨 아래에 여러 줄로 몰려 있고, 특정 코드 줄을 설명하는 게 아니라 전체 접근방식/판단을 서술하는 주석)은 "문제접근"과 "풀이" 섹션을 쓰는 근거로만 사용하고, "전체코드" 섹션에서는 삭제하세요. 같은 내용이 본문과 코드에 중복되면 글이 지저분해집니다.
  - 반대로 특정 코드 줄의 동작을 설명하는 인라인 주석은 남기거나 보강해도 됩니다.
  - 메모 주석을 지운 자리에 생긴 불필요한 빈 줄도 함께 정리해서, 코드블록이 코드로 끝나도록 하세요.
- 코드의 로직과 구조(변수명, 흐름, 알고리즘 자체)는 원본 그대로 유지하고 절대 바꾸지 마세요. 다만 "풀이" 섹션에서 설명한 논리를 코드 안에서도 바로 이해할 수 있도록, 원본에 없던 설명 주석을 추가하거나 짧은 원본 주석을 보강해도 됩니다. 단, 이 주석 역시 코드 주석/README에 실제로 근거한 내용만 담아야 하며 새로운 사실을 지어내지 마세요.
- 문체는 "~함", "~했음", "~판단함" 같은 개조식 종결어미를 섞어 담백한 기술 블로그 톤을 유지하세요.
- "막힌 점 / 배운 점" 같은 섹션은 만들지 마세요. 위 세 섹션(문제접근/풀이/전체코드) 외에는 아무것도 추가하지 마세요.
"""


def build_user_message(
    problem_title: str,
    code: str,
    language: str,
    readme_content: str | None,
    legacy_note_content: str | None,
    topics: list[str] | None = None,
) -> str:
    parts = [f"## 문제명\n{problem_title}\n"]
    parts.append(f"## 코드 ({language}) — 주석에 접근방식/풀이 로직이 담겨 있음\n```{language}\n{code}\n```\n")

    if readme_content:
        parts.append(f"## README (문제 설명)\n{readme_content}\n")
    else:
        parts.append("README가 없습니다. 코드와 문제명만으로 문제 맥락을 최대한 파악하세요.\n")

    if topics:
        # 한글 표기를 함께 주되, 매핑에 없으면 원문 그대로 넘겨 문맥에 맞게 옮기도록 한다.
        rendered = ", ".join(f"{t} ({TOPIC_KO[t]})" if t in TOPIC_KO else t for t in topics)
        parts.append(
            f"## LeetCode 토픽 (해시태그 후보)\n{rendered}\n"
            "이 중 코드에 실제로 쓰인 것만 골라 해시태그로 쓰세요. "
            "이 풀이가 사용하지 않은 접근법은 제외합니다.\n"
        )

    if legacy_note_content:
        parts.append(
            f"## 참고: 레거시 note.md (있다면 보조 자료로 활용)\n{legacy_note_content}\n"
        )

    parts.append(
        "위 코드 주석과 README를 결합해서 '문제 접근'과 '풀이' 섹션을 작성하세요. "
        "코드 주석에 없는 사고 과정은 지어내지 마세요."
    )

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Claude Code 호출 (구독 기반, API 키 미사용)
# ---------------------------------------------------------------------------

def call_claude_code(system_prompt: str, user_message: str) -> str:
    """claude -p (headless 모드)를 subprocess로 호출한다.

    ANTHROPIC_API_KEY 대신 CLAUDE_CODE_OAUTH_TOKEN(구독 인증 토큰)을 사용한다.
    `claude setup-token`으로 발급받은 토큰을 환경변수로 넣어두면 별도 API 과금 없이
    Pro/Max 구독 사용량 한도 안에서 처리된다.
    """
    if shutil.which("claude") is None:
        print(
            "[에러] 'claude' 명령을 찾을 수 없습니다. "
            "Claude Code CLI를 설치하세요: npm install -g @anthropic-ai/claude-code"
        )
        sys.exit(1)

    # 시크릿에 값을 붙여넣을 때 줄바꿈이 섞여 들어오는 일이 잦다(값 중간에 들어가기도 한다).
    # 그대로 두면 CLI가 "Invalid Authorization header value ... contains a line break"로
    # 실패한다. 토큰에는 공백 문자가 들어갈 일이 없으므로 전부 제거하고 넘긴다.
    for key in ("CLAUDE_CODE_OAUTH_TOKEN", "ANTHROPIC_API_KEY"):
        raw = os.environ.get(key)
        if raw:
            cleaned = re.sub(r"\s+", "", raw)
            if cleaned != raw:
                os.environ[key] = cleaned
                print(
                    f"[정리] {key}에 공백/줄바꿈이 섞여 있어 제거했습니다 "
                    f"({len(raw)}자 -> {len(cleaned)}자). 시크릿 값 자체도 고쳐두세요."
                )

    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN") and not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "[경고] CLAUDE_CODE_OAUTH_TOKEN(또는 ANTHROPIC_API_KEY)이 설정되어 있지 않습니다. "
            "구독 인증 토큰은 `claude setup-token`으로 발급받을 수 있습니다."
        )

    cmd = [
        "claude",
        "-p",
        user_message,
        "--append-system-prompt",
        system_prompt,
        "--model",
        MODEL,
        "--output-format",
        "json",
        # 이 호출은 텍스트 생성만 하면 된다. 리포지토리 안에서 실행되기 때문에
        # 도구를 열어두면 기존 posts/ 파일을 직접 고치려 들고, 그 과정에서
        # 권한 거부 안내문이 결과로 돌아와 포스트를 덮어쓰는 일이 생긴다.
        "--disallowed-tools",
        "Read,Write,Edit,Glob,Grep,Bash,WebFetch,WebSearch,Task,NotebookEdit",
    ]

    print("[호출] Claude Code(claude -p) 요청 중... (구독 사용량 사용)")
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=CLAUDE_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        print(f"[에러] claude -p 응답이 {CLAUDE_TIMEOUT_SECONDS}초 내에 오지 않았습니다.")
        sys.exit(1)

    if result.returncode != 0:
        # claude CLI는 인증 실패 등의 에러 메시지를 stderr가 아니라 stdout으로 내보내는
        # 경우가 있다. 둘 다 찍어야 CI 로그에서 원인을 알 수 있다.
        print(f"[에러] claude -p 실행 실패 (exit code {result.returncode})")
        print(f"[stderr] {result.stderr.strip() or '(비어 있음)'}")
        print(f"[stdout] {result.stdout.strip() or '(비어 있음)'}")
        sys.exit(1)

    try:
        response = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("[에러] claude -p 출력이 JSON 형식이 아닙니다. 원본 출력:")
        print(result.stdout)
        print(f"[stderr] {result.stderr.strip() or '(비어 있음)'}")
        sys.exit(1)

    if response.get("is_error"):
        print(f"[에러] claude -p가 에러를 반환했습니다: {response.get('result')}")
        sys.exit(1)

    result_text = response.get("result", "")
    if not result_text:
        print("[에러] claude -p 응답에 result 필드가 비어 있습니다.")
        sys.exit(1)

    return result_text


# ---------------------------------------------------------------------------
# 메인 로직
# ---------------------------------------------------------------------------

EXT_TO_LANG = {
    ".py": "python",
    ".java": "java",
    ".js": "javascript",
    ".ts": "typescript",
    ".cpp": "cpp",
    ".c": "c",
    ".go": "go",
}

# 제목에 쓸 언어 표시명 (코드블록용 소문자 표기와 별도)
LANG_DISPLAY = {
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "cpp": "C++",
    "c": "C",
    "go": "Go",
}


def slugify_title(problem_dir_name: str) -> str:
    # "0383-ransom-note" -> "ransom-note", "42862-체육복" -> "체육복"
    parts = problem_dir_name.split("-", 1)
    return parts[1] if len(parts) == 2 else problem_dir_name


def strip_leading_number(title: str) -> str:
    """'3069. Distribute Elements...' -> 'Distribute Elements...' 처럼 앞의 문제 번호 제거"""
    return re.sub(r"^\s*\d+\.\s*", "", title).strip()


def clean_title_text(text: str) -> str:
    """제목 문자열에서 마크다운/HTML 표기와 앞뒤의 레벨·번호 표기를 제거."""
    text = re.sub(r"^#+\s*", "", text.strip())
    text = re.sub(r"<[^>]+>", "", text).strip()
    # BaekjoonHub 스타일: "[level 1] 제목 - 147355" -> 앞의 [..] 태그, 뒤의 "- 번호" 제거
    text = re.sub(r"^\[[^\]]*\]\s*", "", text)
    text = re.sub(r"\s*-\s*\d+\s*$", "", text)
    return strip_leading_number(text)


def extract_title_from_readme(readme_content: str) -> str | None:
    """README의 첫 헤딩(또는 첫 줄)에서 문제 제목을 추출. 앞뒤의 번호/레벨 표기는 제거.
    예: '# 42862. 체육복' -> '체육복'
        '# [level 1] 크기가 작은 부분문자열 - 147355' -> '크기가 작은 부분문자열'
        '<h2><a href="...">3069. Distribute...</a></h2><h3>Easy</h3>...' -> 'Distribute...'
    """
    # leetcode-sync/BaekjoonHub README는 전체가 한 줄짜리 HTML인 경우가 있다.
    # 줄 단위로 태그만 벗기면 <h2>/<h3>/<p> 텍스트가 전부 이어붙으므로,
    # 첫 HTML 헤딩(<h1>~<h6>)의 내용만 먼저 뽑아본다.
    html_heading = re.search(
        r"<h[1-6][^>]*>(.*?)</h[1-6]>", readme_content, re.IGNORECASE | re.DOTALL
    )
    if html_heading:
        title = clean_title_text(html_heading.group(1))
        if title:
            return title

    for line in readme_content.splitlines():
        title = clean_title_text(line)
        if title:
            return title
    return None


def escape_hashtag_line(text: str) -> str:
    """맨 마지막 해시태그 줄의 '#'을 이스케이프하고 파일 끝 개행을 보장한다.

    마크다운에서 '#배열 #시뮬레이션'은 H1 헤더로 해석되어(티스토리 기본모드 포함)
    본문 맨 아래에 거대한 제목이 생기고 첫 '#'도 사라진다.
    '\\#'로 이스케이프하면 일반 문단 텍스트로 렌더링된다.

    헤더('# 제목' — # 뒤에 공백)와 해시태그('#배열' — # 뒤에 바로 문자)는
    '#' 다음 글자로 구분한다.
    """
    lines = text.rstrip().split("\n")
    for i in range(len(lines) - 1, -1, -1):
        if not lines[i].strip():
            continue
        if re.match(r"^#\S", lines[i].strip()):
            lines[i] = re.sub(r"(?<!\\)#", r"\\#", lines[i])
        break
    return "\n".join(lines) + "\n"


def guess_problem_url(platform: str, problem_dir_name: str) -> str:
    if platform == "leetcode":
        slug = slugify_title(problem_dir_name)
        return f"https://leetcode.com/problems/{slug}/"
    return "(문제 링크를 note.md 또는 여기에 직접 채워주세요)"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_dir", type=str, help="문제 폴더 경로")
    parser.add_argument(
        "--platform",
        choices=["leetcode", "programmers", "baekjoon"],
        default=None,
        help="플랫폼 강제 지정 (자동 판별을 덮어씀)",
    )
    args = parser.parse_args()

    problem_dir = Path(args.problem_dir).resolve()
    if not problem_dir.is_dir():
        print(f"[에러] 폴더를 찾을 수 없습니다: {problem_dir}")
        sys.exit(1)

    platform = detect_platform(problem_dir, args.platform)
    print(f"[판별] 플랫폼: {PLATFORM_LABEL.get(platform, platform)}")

    solution_file = find_solution_file(problem_dir)
    if solution_file is None:
        print(f"[에러] solution 파일을 찾을 수 없습니다: {problem_dir}")
        sys.exit(1)
    print(f"[찾음] 코드 파일: {solution_file.name}")

    readme_file = find_readme_file(problem_dir)
    readme_content = None
    if readme_file:
        readme_content = readme_file.read_text(encoding="utf-8")
        print(f"[찾음] README 있음 -> 문제 설명으로 활용")
    else:
        print(f"[안내] README 없음 -> 코드/문제명만으로 진행")

    note_file = find_note_file(problem_dir)
    legacy_note_content = None
    if note_file:
        legacy_note_content = note_file.read_text(encoding="utf-8")
        print(f"[찾음] 레거시 note.md 있음 -> 보조 자료로 활용")

    code = solution_file.read_text(encoding="utf-8")
    language = EXT_TO_LANG.get(solution_file.suffix, "text")
    problem_title = None
    if readme_content:
        problem_title = extract_title_from_readme(readme_content)
    if not problem_title:
        problem_title = strip_leading_number(slugify_title(problem_dir.name).replace("-", " "))
    problem_url = guess_problem_url(platform, problem_dir.name)

    system_prompt = SYSTEM_PROMPT.format(
        platform=PLATFORM_LABEL.get(platform, platform),
        problem_title=problem_title,
        problem_url=problem_url,
        language=language,
        language_display=LANG_DISPLAY.get(language, language.capitalize()),
    )
    # 토픽은 LeetHub가 루트 README.md에 쌓는 값이라 LeetCode에만 존재한다.
    topics = extract_leetcode_topics(problem_dir.name) if platform == "leetcode" else []
    if topics:
        print(f"[찾음] LeetCode 토픽: {', '.join(topics)}")

    user_message = build_user_message(
        problem_title, code, language, readme_content, legacy_note_content, topics
    )

    result_text = call_claude_code(system_prompt, user_message)

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    def safe_filename_slug(text: str) -> str:
        # 파일명에 쓸 수 없는 문자 제거, 공백은 하이픈으로
        text = re.sub(r"[\\/:*?\"<>|]", "", text)
        return re.sub(r"\s+", "-", text.strip())

    output_name = f"{platform}-{safe_filename_slug(problem_title)}.md"
    output_path = POSTS_DIR / output_name
    output_path.write_text(escape_hashtag_line(result_text), encoding="utf-8")

    print(f"[완료] 저장됨: {output_path}")


if __name__ == "__main__":
    main()
