def maximize(pic, n):
    res = ''
    for i in pic: 
        res += n * i
    return res

def solution(picture, k):
    answer = []
    for i in picture:
        for j in range(k):
            answer.append(maximize(i, k))
    return answer