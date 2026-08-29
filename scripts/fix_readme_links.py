# -*- coding: utf-8 -*-
"""
fix_readme_links.py

LeetHub가 루트 README.md의 토픽 표에 넣는 문제 링크를 실제 폴더 위치에 맞게 고친다.

LeetHub는 자기가 파일을 놓은 자리(리포지토리 루트) 기준으로 링크를 쓰는데,
그 뒤 워크플로우가 폴더를 LeetCode/ 아래로 옮기기 때문에 링크가 어긋난다.
문제를 풀 때마다 새 행이 루트 경로로 추가되므로, 이동 직후 매번 실행해서 바로잡는다.

고치는 것:
  tree/master/...            -> tree/main/...        (master 브랜치는 더 이상 없음)
  tree/main/0020-foo         -> tree/main/LeetCode/0020-foo
  tree/main/LeetCode/Easy/.. -> tree/main/LeetCode/..  (예전 난이도 폴더 구조 잔재)

이미 올바른 링크는 그대로 두므로 반복 실행해도 안전하다.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"

# LeetHub가 관리하는 블록. 이 바깥(프로젝트 설명)은 건드리지 않는다.
BLOCK_RE = re.compile(
    r"(<!---LeetCode Topics Start-->)(.*?)(<!---LeetCode Topics End-->)", re.DOTALL
)


def fix_links(block: str) -> str:
    # 1) 기본 브랜치 통일
    block = re.sub(r"(/tree/)master(/)", r"\1main\2", block)
    # 2) 난이도 폴더 구조 잔재 제거 (LeetCode/Easy/0020-... -> LeetCode/0020-...)
    block = re.sub(
        r"(/tree/main/LeetCode/)(?:Easy|Medium|Hard)/(?=\d)", r"\1", block
    )
    # 3) 루트 경로로 적힌 문제 폴더를 LeetCode/ 아래로
    #    이미 LeetCode/가 붙어 있으면 매치되지 않는다.
    block = re.sub(r"(/tree/main/)(?=\d{4}-)", r"\1LeetCode/", block)
    return block


def main() -> int:
    if not README.exists():
        print("[건너뜀] README.md가 없습니다.")
        return 0

    content = README.read_text(encoding="utf-8")
    match = BLOCK_RE.search(content)
    if not match:
        print("[건너뜀] LeetCode Topics 블록을 찾지 못했습니다.")
        return 0

    fixed_block = fix_links(match.group(2))
    if fixed_block == match.group(2):
        print("[변경 없음] 링크가 이미 모두 올바릅니다.")
        return 0

    updated = content[: match.start(2)] + fixed_block + content[match.end(2) :]
    README.write_text(updated, encoding="utf-8")

    before = set(re.findall(r"https://github\.com/\S+?/tree/\S+?(?=\))", match.group(2)))
    after = set(re.findall(r"https://github\.com/\S+?/tree/\S+?(?=\))", fixed_block))
    print(f"[수정] README 링크 갱신: {len(before - after)}개 경로 변경")
    return 0


if __name__ == "__main__":
    sys.exit(main())
