# [LeetCode] Roman to Integer (Python 풀이)

## 문제접근
https://leetcode.com/problems/roman-to-integer/

로마 숫자는 I, V, X, L, C, D, M 일곱 개의 기호로 구성되며 각 기호는 정해진 값을 가진다.

기본적으로는 왼쪽부터 오른쪽으로 값을 더해가면 되지만, IV나 IX처럼 작은 값이 큰 값 앞에 오는 경우에는 큰 값에서 작은 값을 빼는 예외 규칙이 있다.

문제 조건에 맞춰서 구현하면 될 것 같다고 판단했고, 현재 위치의 숫자보다 바로 뒤에 오는 숫자가 더 크면 뒤 값에서 현재 값을 빼서 더하고 인덱스를 두 칸 건너뛰는 방식으로 처리하면 될 것 같다고 생각했다.

전체 문자열을 while문으로 돌면서 인덱스를 직접 관리하는 방식을 택했고, 각 기호의 값을 조회할 때 성능을 높이기 위해 사전(dict)을 만들어서 사용하면 좋을 것 같다고 판단했다.

## 풀이

**1.** 로마 숫자 기호와 값을 매핑한 딕셔너리를 미리 만들어 조회 성능을 확보한다.

**2.** answer와 idx를 0으로 초기화하고 while문으로 문자열 끝까지 순회한다.

**3.** 현재 인덱스가 마지막 문자가 아니고, 현재 문자의 값이 다음 문자의 값보다 작으면 감산 규칙(IV, IX 등)에 해당하므로 다음 값에서 현재 값을 뺀 만큼 answer에 더하고 idx를 2 증가시킨다.

**4.** 그렇지 않으면 현재 문자의 값을 그대로 answer에 더하고 idx를 1 증가시킨다.

**5.** 순회가 끝나면 answer를 반환한다.

## 전체코드
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        idx = 0
        
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        while (idx < len(s)):
            # 현재 값이 다음 값보다 작으면 감산 규칙(IV, IX 등) 적용
            if (idx < len(s)-1 and dict[s[idx]] < dict[s[idx+1]]):
                answer += dict[s[idx+1]] - dict[s[idx]]
                idx += 2
            else:
                answer += dict[s[idx]]
                idx += 1

        return answer
```

\#문자열 \#해시맵
