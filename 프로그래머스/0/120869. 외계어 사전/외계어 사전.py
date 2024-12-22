def solution(spell, dic):
    answer = 0
    for d in dic:
        print(set(spell), set(d))
        if (set(spell) == set(d)):
            answer = 1
            break
        else:
            answer = 2
    return answer