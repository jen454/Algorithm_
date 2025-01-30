def solution(arr):
    row = len(arr)
    col = len(arr[0])
    # 행의 수 > 열의 수
    if (row > col):
        for i in range(row):
            for j in range(row- col):
                arr[i].append(0)
    # 행의 수 < 열의 수
    elif (row < col):
        for i in range(col - row):
            arr.append([0 for j in range(col)])
    return arr