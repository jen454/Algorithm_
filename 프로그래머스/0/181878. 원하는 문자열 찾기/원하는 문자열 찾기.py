def solution(myString, pat):
    answer = 0
    if (len(myString) >= len(pat) and pat.lower() in myString.lower()):
        answer = 1
    return answer