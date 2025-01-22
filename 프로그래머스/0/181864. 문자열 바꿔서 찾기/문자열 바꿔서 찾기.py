def solution(myString, pat):
    answer = 0
    newString = ''
    for i in myString:
        if (i == 'A'):
            newString += 'B'
        else:
            newString += 'A'
    if (pat in newString):
        answer = 1
    return answer