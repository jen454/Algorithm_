def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if (number[i]+number[j]+number[k] == 0):
                    answer += 1
    return answer

# 삼중 포문으로 돌면서 카운트를 세면 되지 않을까?
# 첫번째 포문은 전체 길이 - 2까지
# 두번째 포문은 첫번째 +1 부터 전체 길이 -1까지
# 세번째 포문은 두번째 +1 부터 전체길이까지