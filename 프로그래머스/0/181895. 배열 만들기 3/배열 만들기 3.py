def solution(arr, intervals):
    answer = []
    intarr = []
    for r in intervals:
        intarr.append(arr[r[0]:r[1]+1])
    answer = intarr[0] + intarr[1]
    return answer