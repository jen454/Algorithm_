import re

def solution(myStr):
    answer = []
    for i in re.split('[a|b|c]', myStr):
        if (i != ""):
            answer.append(i)
    if (len(answer) == 0):
        answer.append('EMPTY')
    return answer