def solution(a, b):
    answer = 0
    sum1 = int(str(a) + str(b))
    sum2 = 2 * a * b
    if (sum1 != sum2):
        answer = max(sum1, sum2)
    else:
        answer = sum1
    return answer