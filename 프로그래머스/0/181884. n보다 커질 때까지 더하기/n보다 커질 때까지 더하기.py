def solution(numbers, n):
    answer = 0
    for i in numbers:
        if (n < answer):
            return answer
        answer += i
    return answer