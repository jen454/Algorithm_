def solution(n):
    answer = 0
    answer = (''.join(sorted(str(n))[::-1]))
    answer = int(answer)
    return answer