def solution(a, b):
    answer = 0
    for num in range(min(a,b),max(a,b)+1):
        answer += num
    return answer