def solution(t, p):
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        if (int(t[i:i+len(p)]) <= int(p)):
            answer += 1
    return answer

## 조건대로 따라서 푸는 시뮬레이션인듯하다.
## t 문자열 길이에서 p 문자열 길이를 뺀 만큼 순회하면서 p 문자열 길이만큼 파싱해서 p랑 정수로 변환후 비교해서 카운트 세기