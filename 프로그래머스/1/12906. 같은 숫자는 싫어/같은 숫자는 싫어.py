def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if (answer[-1] == i):
            pass
        else:
            answer.append(i)
    return answer