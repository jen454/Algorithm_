def solution(s):
    answer = True
    s = s.lower() 
    if ((s.count("p") != 0 or s.count("y") != 0) and s.count("p") != s.count("y")):
        answer = False
    return answer

