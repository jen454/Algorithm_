def solution(arr):
    twoArr = []
    for i in range(len(arr)):
        if (arr[i] == 2):
            twoArr.append(i)
    if (len(twoArr) == 0):
        return [-1]
    else:
        return arr[twoArr[0]:twoArr[-1]+1]