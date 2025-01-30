def solution(myString):
    answer = ''
    prevI = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    for i in myString:
        if (i in prevI):
            answer += 'l'
        else:
            answer += i
    return answer