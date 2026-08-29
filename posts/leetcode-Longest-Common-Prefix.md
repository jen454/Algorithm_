# [LeetCode] Longest Common Prefix (Python 풀이)

## 문제접근
https://leetcode.com/problems/longest-common-prefix/

문자열 배열이 주어졌을 때 모든 문자열에 공통으로 들어가는 가장 긴 접두사를 찾는 문제임.

공통 접두사가 없다면 빈 문자열을 반환해야 함.

배열 안에서 가장 짧은 길이의 문자열을 기준으로 비교하면 되지 않을까 하는 생각에서 접근을 시작함.

가장 짧은 문자열보다 긴 접두사는 애초에 존재할 수 없기 때문에, 정렬을 통해 가장 짧은 길이의 문자열을 먼저 추출함.

이후 이 가장 짧은 문자열을 기준으로 나머지 문자열들을 순회하면서 같은 위치의 문자가 일치하는지 확인하는 방식으로 풀이 방향을 잡음.

앞에서부터 모든 문자열의 문자가 같으면 answer에 추가하고, 다르면 그 전까지 쌓인 배열을 반환하는 흐름으로 구현함.

## 풀이

**1.** strs를 길이 기준으로 정렬해서 가장 짧은 문자열을 shortest로 추출한다.

**2.** shortest의 각 문자를 인덱스와 함께 순회한다.

**3.** 같은 인덱스에서 나머지 문자열들(strs[1:])의 문자와 shortest의 문자를 비교한다.

**4.** 하나라도 문자가 다르면 그 시점까지 answer에 쌓인 문자들을 합쳐서 바로 반환한다.

**5.** 모든 문자열이 해당 인덱스에서 같은 문자를 가지면 answer에 그 문자를 추가한다.

**6.** 끝까지 순회를 마치면 answer에 쌓인 문자들을 합쳐서 반환한다.

## 전체코드
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        # 가장 짧은 문자열보다 긴 공통 접두사는 존재할 수 없으므로
        # 길이 기준으로 정렬해서 가장 짧은 문자열을 기준으로 삼는다.
        strs.sort(key=len)
        shortest = strs[0]

        for i, char in enumerate(shortest):
            # shortest를 기준으로 나머지 문자열들의 같은 위치 문자를 비교한다.
            for s in strs[1:]:
                if s[i] != char:
                    # 문자가 다르면 그 전까지 쌓인 배열을 반환한다.
                    return "".join(answer)
            # 앞에서부터 모두 같으면 answer에 추가
            answer.append(char)

        return "".join(answer)
```

\#문자열 \#정렬
