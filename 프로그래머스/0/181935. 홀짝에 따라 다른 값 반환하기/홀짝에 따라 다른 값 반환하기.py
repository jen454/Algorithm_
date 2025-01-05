def solution(n):
    answer = 0
    if (n % 2):
        for i in range(1, n+1):
            if (i % 2):
                answer += i
    else:
        for i in range(1, n+1):
            if (i % 2 == 0):
                answer += i * i
    return answer