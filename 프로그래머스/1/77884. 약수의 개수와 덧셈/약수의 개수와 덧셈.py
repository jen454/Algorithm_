import math
def check(number):
    arr = []
    for num in range(1,int(math.sqrt(number))+1):
        if (number % num == 0):
            if (math.sqrt(number) == num):
                arr.append(num);
            else:
                arr.append(num);
                arr.append(number // num);
    return len(arr)

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if (check(i) % 2 == 0):
            answer += i
        else:
            answer -= i
    return answer