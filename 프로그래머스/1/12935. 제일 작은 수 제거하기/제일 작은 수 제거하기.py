def solution(arr):
    answer = []
    arr.pop(arr.index(min(arr)))
    if (len(arr)):
        answer = arr
    else: 
        answer = [-1]
    return answer