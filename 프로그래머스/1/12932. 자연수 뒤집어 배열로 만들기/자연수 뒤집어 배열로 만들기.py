def solution(n):
    answer = []
    res = str(n)[::-1]
    print(res)
    for i in res:
        answer.append(int(i))
    return answer