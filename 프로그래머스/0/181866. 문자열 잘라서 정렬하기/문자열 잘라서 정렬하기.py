def solution(myString):
    answer = []
    for i in myString.split('x'):
        if (i != ''):
            answer.append(i)
    answer.sort()
    return answer