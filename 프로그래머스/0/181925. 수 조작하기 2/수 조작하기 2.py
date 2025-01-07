def solution(numLog):
    answer = ''
    prev = 0
    for n in numLog:
        if ((n - prev) == 1):
            answer += 'w'
        elif ((n - prev) == -1):
            answer += 's'
        elif ((n - prev) == 10):
            answer += 'd'
        elif ((n - prev) == -10):
            answer += 'a'
        prev = n
    return answer