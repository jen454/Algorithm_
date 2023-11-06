def solution(x):
    answer = False
    sum = 0
    for i in str(x):
        sum += int(i)
    if (x % sum == 0):
        answer = True
    return answer