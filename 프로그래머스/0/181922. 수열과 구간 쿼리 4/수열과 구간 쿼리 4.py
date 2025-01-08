def solution(arr, queries):
    for q in queries:
        for i in range(len(arr)):
            if ((i in range(q[0], q[1]+1)) and (i % q[2] == 0)):
                arr[i] += 1
    return arr