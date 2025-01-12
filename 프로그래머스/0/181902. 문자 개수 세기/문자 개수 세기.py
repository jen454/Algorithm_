def solution(my_string):
    answer = [0 for i in range(52)]
    for s in my_string:
        if (ord(s) in range(65,91)):
            answer[ord(s)-65] += 1
        elif (ord(s) in range(97,123)):
            answer[ord(s)-71] += 1
    return answer
# 대문자 65~90
# 소문자 97~122