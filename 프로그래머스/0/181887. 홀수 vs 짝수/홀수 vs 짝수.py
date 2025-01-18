def solution(num_list):
    answer = 0
    a = 0
    b = 0
    for i in range(1, len(num_list)+1):
        if (i % 2 == 0):
            a += num_list[i-1]
        else:
            b += num_list[i-1]
    answer = max(a,b)
    return answer