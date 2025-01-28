def solution(n_str):
    i = 0
    while 1:
        if (n_str[i] == '0'):
            i += 1
        else:
            break
    return n_str[i:]