def solution(my_string, m, c):
    answer = ''
    s = ''
    arr = []
    for i in range(1, len(my_string)+1):
        s += my_string[i-1]
        if (i % m == 0):
            arr.append(s)
            s = ''
    for i in arr:
        answer += i[c-1]
    return answer