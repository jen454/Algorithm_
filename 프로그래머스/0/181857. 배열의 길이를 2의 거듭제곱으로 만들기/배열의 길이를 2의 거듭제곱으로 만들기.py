def solution(arr):
    i = 0
    while 1:
        if (len(arr) > 2**i):
            i += 1
        else:
            arr += [0] * (2**i - len(arr))
            return arr