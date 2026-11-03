# Algorithm_

알고리즘 문제를 풀면 **블로그 포스트 초안이 자동으로 생성되는** 저장소입니다.

브라우저 확장이 풀이를 push하면 → GitHub Actions가 폴더를 정리하고 → Claude Code가 코드와 주석을 읽어 포스트 초안을 `posts/`에 커밋합니다. 초안을 검토한 뒤 티스토리에 붙여넣어 발행합니다.

**초안까지만 자동화한 이유**: 티스토리 Open API가 종료되어 완전 자동 발행이 불가능하고, 글의 품질은 사람이 책임져야 한다고 판단했습니다. 그래서 사람의 검토를 마지막 관문으로 두었습니다.

## 어떻게 돌아가나

```
LeetCode 풀이 → LeetHub가 루트에 커밋 (README와 코드가 별도 커밋)
                     ↓
   main.yml : LeetCode/ 아래로 이동 + README 토픽 표 링크 보정
                     ↓
   README와 코드가 모두 모였을 때만 → generate_post.py : claude -p 호출
                     ↓
              posts/*.md 자동 커밋

백준/프로그래머스 풀이 → BaekjoonHub가 커밋
                     ↓
    generate-post-non-leetcode.yml : 바뀐 문제 폴더만 감지 → 위와 동일
```

포스트는 **코드에 직접 쓴 주석**을 근거로 작성됩니다. 접근방식을 주석으로 남겨두면 그게 그대로 "문제접근" 섹션이 되므로, 별도 메모 파일은 필요 없습니다.

## 구조

| 경로 | 설명 |
| --- | --- |
| `LeetCode/` | LeetHub가 올린 풀이 (워크플로우가 루트에서 옮겨옴) |
| `백준/`, `프로그래머스/` | BaekjoonHub가 올린 풀이 |
| `posts/` | 자동 생성된 블로그 포스트 초안 |
| `scripts/generate_post.py` | 포스트 생성 스크립트 (README·코드 파싱, 프롬프트 구성, `claude -p` 호출) |
| `scripts/fix_readme_links.py` | LeetHub 토픽 표의 링크를 이동된 폴더 위치에 맞게 보정 (멱등) |
| `.github/workflows/main.yml` | LeetCode: 폴더 이동 → 포스트 생성 |
| `.github/workflows/generate-post-non-leetcode.yml` | 백준/프로그래머스: 변경 감지 → 포스트 생성 |

## 생성되는 포스트 형식

`문제접근` / `풀이` / `전체코드` 세 섹션과 해시태그 한 줄로 고정됩니다. 해시태그는 아래 LeetCode Topics 표에서 해당 문제의 토픽을 가져오되, 실제 코드에 쓰이지 않은 기법은 제외합니다.

예시: [Valid Parentheses](posts/leetcode-Valid-Parentheses.md) · [Roman to Integer](posts/leetcode-Roman-to-Integer.md) · [삼총사](posts/programmers-삼총사.md)

## 설계 원칙

- **AI는 재구성만 합니다.** 코드·주석·README에 있는 내용만 글로 옮기고, 거기 없는 추론·과장·태그는 만들지 않도록 프롬프트 전 섹션에 제약을 걸었습니다.
- **AI는 텍스트만 생성합니다.** `--disallowed-tools`로 파일 도구를 막아 모델이 저장소 파일을 직접 수정하지 못하게 했습니다. 파일 저장은 스크립트가 맡습니다.
- **엔진 선택**: 하루 2~3문제 규모에서는 종량제 API보다 기존 구독 기반 Claude Code CLI(headless)가 경제적이라 판단했습니다.

## 안정성 장치

| 문제 | 대응 |
| --- | --- |
| LeetHub가 README와 코드를 약 1초 간격으로 따로 커밋 | 두 파일이 모두 있을 때만 생성 (`find` 가드) |
| 연속 커밋으로 워크플로우가 겹쳐 push 경합 | `concurrency`로 직렬화, 실패 시 원격 최신 상태에서 재계산 후 재시도 |
| CLI 오류가 stdout으로 나와 CI 로그에 안 남음 | 실패 시 stdout/stderr 모두 출력, 인증 스모크 테스트 스텝 |
| Secrets 토큰에 섞인 줄바꿈으로 인증 실패 | 공백 문자 제거 후 사용, 정리 전후 길이 로깅 |
| `GITHUB_TOKEN` 기본 권한이 읽기 전용 | `permissions: contents: write` 명시 |
| 한글 경로가 `\355\225...`로 이스케이프됨 | `git -c core.quotePath=false` |

## 직접 실행하기

특정 문제의 포스트를 수동으로 만들려면:

```bash
python scripts/generate_post.py LeetCode/0020-valid-parentheses
```

인증은 API 키가 아니라 Claude 구독을 사용합니다. `claude setup-token`으로 발급받은 값을 환경변수 `CLAUDE_CODE_OAUTH_TOKEN`에 넣으면 되고, GitHub Actions에서는 같은 이름의 리포지토리 시크릿으로 등록합니다. 값에 줄바꿈이 섞여도 스크립트가 제거하지만, 가능하면 한 줄로 붙여넣으세요.

---

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
| Problem Name | Difficulty |
| ------- | ------- |
| [0001-two-sum](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0001-two-sum/) | Easy |
| [0014-longest-common-prefix](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0014-longest-common-prefix/) | Easy |
| [1480-running-sum-of-1d-array](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1480-running-sum-of-1d-array/) | Easy |
| [1672-richest-customer-wealth](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1672-richest-customer-wealth/) | Easy |
| [3069-distribute-elements-into-two-arrays-i](https://github.com/jen454/Algorithm_/tree/main/LeetCode/3069-distribute-elements-into-two-arrays-i/) | Easy |
## Prefix Sum
| Problem Name | Difficulty |
| ------- | ------- |
| [1480-running-sum-of-1d-array](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1480-running-sum-of-1d-array/) | Easy |
## Matrix
| Problem Name | Difficulty |
| ------- | ------- |
| [1672-richest-customer-wealth](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1672-richest-customer-wealth/) | Easy |
## Math
| Problem Name | Difficulty |
| ------- | ------- |
| [0009-palindrome-number](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0009-palindrome-number/) | Easy |
| [0013-roman-to-integer](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0013-roman-to-integer/) | Easy |
| [0412-fizz-buzz](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0412-fizz-buzz/) | Easy |
## String
| Problem Name | Difficulty |
| ------- | ------- |
| [0013-roman-to-integer](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0013-roman-to-integer/) | Easy |
| [0014-longest-common-prefix](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0014-longest-common-prefix/) | Easy |
| [0020-valid-parentheses](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0020-valid-parentheses/) | Easy |
| [0383-ransom-note](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0383-ransom-note/) | Easy |
| [0412-fizz-buzz](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0412-fizz-buzz/) | Easy |
## Simulation
| Problem Name | Difficulty |
| ------- | ------- |
| [0412-fizz-buzz](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0412-fizz-buzz/) | Easy |
| [3069-distribute-elements-into-two-arrays-i](https://github.com/jen454/Algorithm_/tree/main/LeetCode/3069-distribute-elements-into-two-arrays-i/) | Easy |
## Hash Table
| Problem Name | Difficulty |
| ------- | ------- |
| [0001-two-sum](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0001-two-sum/) | Easy |
| [0013-roman-to-integer](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0013-roman-to-integer/) | Easy |
| [0383-ransom-note](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0383-ransom-note/) | Easy |
## Counting
| Problem Name | Difficulty |
| ------- | ------- |
| [0383-ransom-note](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0383-ransom-note/) | Easy |
## Trie
| Problem Name | Difficulty |
| ------- | ------- |
| [0014-longest-common-prefix](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0014-longest-common-prefix/) | Easy |
## Stack
| Problem Name | Difficulty |
| ------- | ------- |
| [0020-valid-parentheses](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0020-valid-parentheses/) | Easy |
## Bracket Sequences
| Problem Name | Difficulty |
| ------- | ------- |
| [0020-valid-parentheses](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0020-valid-parentheses/) | Easy |
<!---LeetCode Topics End-->
