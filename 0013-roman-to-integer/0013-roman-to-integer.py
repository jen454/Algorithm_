class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        idx = 0
        
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        while (idx < len(s)):
            if (idx < len(s)-1 and dict[s[idx]] < dict[s[idx+1]]):
                answer += dict[s[idx+1]] - dict[s[idx]]
                idx += 2
            else:
                answer += dict[s[idx]]
                idx += 1

        return answer

# 문제 조건에 맞춰서 구현하면 되는 것 같다.
# 현재 숫자보다 뒤에 숫자가 더 크면 뒤 - 현재 값으로 계산하고 인덱스 건너뛰기
# while문 돌려서 인덱스 관리하면 될 것 같음
# 사전을 만들어서 조회 성능 올리면 좋을듯