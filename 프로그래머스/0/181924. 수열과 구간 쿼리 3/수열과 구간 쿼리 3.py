def solution(arr, queries):
    answer = [i for i in arr]
    for q in queries:
        prev1 = arr[q[1]]
        prev2 = arr[q[0]]
        answer[q[0]] = prev1
        answer[q[1]] = prev2
        arr = answer
    return answer