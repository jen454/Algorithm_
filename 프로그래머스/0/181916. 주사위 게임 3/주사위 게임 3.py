def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    dict_arr = dict()

    for d in dice:
        if d not in dict_arr:
            dict_arr[d] = 1
        else:
            dict_arr[d] += 1

    dict_arr = sorted(dict_arr, key=lambda x: dict_arr[x])

    # case 1
    if len(dict_arr) == 1:
        answer = 1111 * a
    # case 2, 3
    elif len(dict_arr) == 2:
        if dice.count(dict_arr[0]) in [1, 3]:
            answer = (10 * dict_arr[1] + dict_arr[0]) ** 2
        else:
            answer = (dict_arr[0] + dict_arr[1]) * abs(dict_arr[0] - dict_arr[1])
    # case 4
    elif len(dict_arr) == 3:
        answer = dict_arr[0] * dict_arr[1]
    # case 5
    elif len(dict_arr) == 4:
        answer = min(dice)
    return answer
