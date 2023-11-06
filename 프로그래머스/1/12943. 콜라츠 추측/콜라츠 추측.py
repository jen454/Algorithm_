def solution(num):
    answer = 0
    base = 500
    while (base):
        if (num == 1):
            break
        if (num % 2 == 0):
            num /= 2
            answer += 1
        elif (num % 2 != 0):
            num = (num*3)+1
            answer += 1
        base -= 1
    if (answer == 500): answer = -1
    return answer