def solution(num_list, n):
    prev = []
    next = []
    for i in range(len(num_list)):
        if (i >= n):
            prev.append(num_list[i])
        else:
            next.append(num_list[i])
    return prev + next