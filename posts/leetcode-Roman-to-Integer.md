# [LeetCode] Roman to Integer (Python 풀이)

## 문제접근

https://leetcode.com/problems/roman-to-integer/

주석에 적힌 대로 문제 조건에 맞춰 그대로 구현하면 되는 문제로 판단함.

핵심은 현재 인덱스의 문자가 다음 인덱스의 문자보다 값이 작을 때, 즉 뺄셈 표기법인 경우를 구분해서 처리하는 것이다.

이 경우에는 뒤 값에서 현재 값을 빼서 더하고 인덱스를 2칸 건너뛰고, 그렇지 않으면 현재 값을 그대로 더하고 1칸만 이동하는 방식으로 접근함.

또한 문자마다 값을 조회해야 하므로 딕셔너리를 만들어서 조회 성능을 높이면 좋을 것 같다고 판단함.

## 풀이

**1.** 로마 숫자 문자와 값을 매핑하는 딕셔너리를 만든다.

**2.** while문으로 idx를 0부터 문자열 끝까지 이동하며 순회한다.

**3.** 현재 idx가 마지막 인덱스가 아니면서, 현재 문자의 값이 다음 문자의 값보다 작은 경우 뺄셈 표기법(IV, IX 등)으로 판단하고 다음 값 - 현재 값을 answer에 더한 뒤 idx를 2 증가시킨다.

**4.** 그 외의 경우에는 현재 문자의 값을 그대로 answer에 더하고 idx를 1 증가시킨다.

**5.** 순회가 끝나면 answer를 반환한다.

## 전체코드

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        idx = 0

        # 문자마다 값을 조회해야 하므로 딕셔너리로 조회 성능을 올림
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        while (idx < len(s)):
            # 현재 숫자보다 뒤에 숫자가 더 크면(뺄셈 표기법) 뒤 - 현재 값으로 계산하고 인덱스 2칸 건너뛰기
            if (idx < len(s)-1 and dict[s[idx]] < dict[s[idx+1]]):
                answer += dict[s[idx+1]] - dict[s[idx]]
                idx += 2
            else:
                # 일반적인 경우 현재 값을 그대로 더하고 1칸 이동
                answer += dict[s[idx]]
                idx += 1

        return answer
```

\#문자열 \#해시맵 \#시뮬레이션
