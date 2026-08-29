# [LeetCode] Longest Common Prefix (Python 풀이)

## 문제접근
https://leetcode.com/problems/longest-common-prefix/

이 문제는 문자열 배열이 주어졌을 때 모든 문자열에 공통으로 존재하는 가장 긴 접두사를 찾는 문제이다.

공통 접두사가 없다면 빈 문자열을 반환해야 한다.

배열 안에서 가장 짧은 길이를 기준으로 비교하면서 보면 되지 않을까 하는 생각에서 접근을 시작했다.

그래서 먼저 정렬을 해서 제일 짧은 길이의 문자열을 추출한다.

제일 짧은 길이의 문자열을 기준으로 다른 문자열 배열을 순회하면서 같은 위치의 문자가 다른 원소가 있는지 체크한다.

앞에서부터 모두 같으면 answer에 그 문자를 추가하고, 다르면 그 전까지 만들어둔 answer를 반환하는 방식으로 풀었다.

## 풀이
**1.** strs를 길이 기준으로 정렬해서 가장 짧은 문자열을 shortest로 삼는다.

가장 짧은 문자열이 전체 공통 접두사의 최대 길이를 제한하기 때문이다.

**2.** shortest를 인덱스와 함께 순회하면서, 같은 인덱스의 문자를 나머지 문자열들과 비교한다.

**3.** 비교 중 한 곳이라도 문자가 다르면 그 시점까지 answer에 쌓인 문자들을 join해서 바로 반환한다.

**4.** 끝까지 모든 문자가 일치했다면 answer에 해당 문자를 추가하고 다음 인덱스로 넘어간다.

**5.** shortest의 끝까지 순회가 끝나면 answer를 join해서 반환한다.

## 전체코드
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        strs.sort(key=len)  # 가장 짧은 문자열을 기준으로 삼기 위해 길이순 정렬
        shortest = strs[0]

        for i, char in enumerate(shortest):
            for s in strs[1:]:
                if s[i] != char:  # 같은 인덱스에서 문자가 다르면 여기까지가 공통 접두사
                    return "".join(answer)
            answer.append(char)  # 모든 문자열에서 일치하면 answer에 추가

        return "".join(answer)
```

\#배열 \#문자열
