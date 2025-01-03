def solution(my_string, overwrite_string, s):
    answer = ''
    f_string = my_string[0:s]
    b_string = my_string[len(overwrite_string)+s:]
    answer = f_string + overwrite_string + b_string
    return answer