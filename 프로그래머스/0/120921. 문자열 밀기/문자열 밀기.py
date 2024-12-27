def solution(A, B):
    answer = 0
    twoB = B+B
    if (twoB.find(A) != -1):
        answer = twoB.find(A)
    else:
        answer = -1
    return answer