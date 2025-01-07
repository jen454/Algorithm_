def solution(arr, queries):
    answer = []
    res = []
    for q in queries:
        for i in range(len(arr)):
            if ((i in range(q[0], q[1]+1)) and (arr[i] > q[2])):
                res.append(arr[i])
        if (res != []):
            answer.append(min(res))
        else:
            answer.append(-1)
        res = []
    return answer