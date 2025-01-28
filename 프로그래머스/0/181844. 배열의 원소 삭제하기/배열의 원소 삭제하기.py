def solution(arr, delete_list):
    for i in delete_list:
        if (i in arr):
            arr.pop(arr.index(i))
    return arr