def solution(polynomial):
    answer = ''
    p_num = 0
    n_num = 0
    # 변수, 상수 추출
    arr = polynomial.split()
    # 변수 합, 상수 합 추출
    for i in arr:
        if (i == '+'):
            continue
        elif (i[-1] == 'x'):
            if (i == 'x'):
                p_num += 1
            else:
                p_num += int(i[0:-1])
        else:
            n_num += int(i)
    # 다항식 계산
    if (p_num == 0 and n_num != 0):
        answer = str(n_num)
    elif (p_num != 0 and n_num == 0):
        if (p_num == 1):
            answer = "x"
        else:
            answer = str(p_num) + "x"
    else:
        if (p_num == 1):
            answer = "x + " + str(n_num)
        else:
            answer = str(p_num) + "x + " + str(n_num)
    return answer