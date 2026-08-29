# Algorithm_

알고리즘 문제를 풀면 **블로그 포스트 초안이 자동으로 생성되는** 저장소입니다.

브라우저 확장이 풀이를 push하면 → GitHub Actions가 폴더를 정리하고 → Claude Code가 코드와 주석을 읽어 포스트를 써서 `posts/`에 커밋합니다. 문제를 푼 뒤 따로 할 일은 없습니다.

## 어떻게 돌아가나

```
LeetCode 풀이 → LeetHub가 루트에 커밋
                     ↓
              main.yml : LeetCode/ 아래로 이동
                     ↓
        scripts/generate_post.py : claude -p 호출
                     ↓
              posts/*.md 자동 커밋

백준/프로그래머스 풀이 → BaekjoonHub가 커밋
                     ↓
    generate-post-non-leetcode.yml : 바뀐 폴더만 감지 → 위와 동일
```

포스트는 **코드에 직접 쓴 주석**을 근거로 작성됩니다. 접근방식을 주석으로 남겨두면 그게 그대로 "문제접근" 섹션이 되므로, 별도 메모 파일은 필요 없습니다.

## 구조

| 경로 | 설명 |
| --- | --- |
| `LeetCode/` | LeetHub가 올린 풀이 (워크플로우가 루트에서 옮겨옴) |
| `백준/`, `프로그래머스/` | BaekjoonHub가 올린 풀이 |
| `posts/` | 자동 생성된 블로그 포스트 초안 |
| `scripts/generate_post.py` | 포스트 생성 스크립트 |
| `.github/workflows/` | 자동화 워크플로우 2종 |

## 생성되는 포스트 형식

`문제접근` / `풀이` / `전체코드` 세 섹션과 해시태그 한 줄로 고정됩니다. 해시태그는 아래 LeetCode Topics 표에서 해당 문제의 토픽을 가져오되, 실제 코드에 쓰이지 않은 기법은 제외합니다.

## 직접 실행하기

특정 문제의 포스트를 수동으로 만들려면:

```bash
python scripts/generate_post.py LeetCode/0020-valid-parentheses
```

인증은 API 키가 아니라 Claude 구독을 사용합니다. `claude setup-token`으로 발급받은 값을 환경변수 `CLAUDE_CODE_OAUTH_TOKEN`에 넣으면 되고, GitHub Actions에서는 같은 이름의 리포지토리 시크릿으로 등록합니다. 값에 줄바꿈이 섞이면 인증이 실패하므로 주의하세요.

---

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
| Problem Name | Difficulty |
| ------- | ------- |
| [0001-two-sum](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0001-two-sum/) | Easy |
| [0014-longest-common-prefix](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0014-longest-common-prefix/) | Easy |
| [1480-running-sum-of-1d-array](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1480-running-sum-of-1d-array) |
| [1672-richest-customer-wealth](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1672-richest-customer-wealth) |
| [3069-distribute-elements-into-two-arrays-i](https://github.com/jen454/Algorithm_/tree/main/LeetCode/3069-distribute-elements-into-two-arrays-i/) | Easy |
## Prefix Sum
| Problem Name | Difficulty |
| ------- | ------- |
| [1480-running-sum-of-1d-array](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1480-running-sum-of-1d-array) |
## Matrix
| Problem Name | Difficulty |
| ------- | ------- |
| [1672-richest-customer-wealth](https://github.com/jen454/Algorithm_/tree/main/LeetCode/1672-richest-customer-wealth) |
## Math
| Problem Name | Difficulty |
| ------- | ------- |
| [0009-palindrome-number](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0009-palindrome-number/) | Easy |
| [0013-roman-to-integer](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0013-roman-to-integer/) | Easy |
| [0412-fizz-buzz](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0412-fizz-buzz) |
## String
| Problem Name | Difficulty |
| ------- | ------- |
| [0013-roman-to-integer](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0013-roman-to-integer/) | Easy |
| [0014-longest-common-prefix](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0014-longest-common-prefix/) | Easy |
| [0020-valid-parentheses](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0020-valid-parentheses/) | Easy |
| [0383-ransom-note](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0383-ransom-note/) | Easy |
| [0412-fizz-buzz](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0412-fizz-buzz) |
## Simulation
| Problem Name | Difficulty |
| ------- | ------- |
| [0412-fizz-buzz](https://github.com/jen454/Algorithm_/tree/main/LeetCode/0412-fizz-buzz) |
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
