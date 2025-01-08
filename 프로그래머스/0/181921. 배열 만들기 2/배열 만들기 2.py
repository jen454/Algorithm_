def solution(l, r):
    answer = []
    five = ['0', '5']
    for n in range(l, r+1):
        if all(num in five for num in str(n)):
            answer.append(n)
    if (len(answer) == 0):
        answer.append(-1)
    return answer