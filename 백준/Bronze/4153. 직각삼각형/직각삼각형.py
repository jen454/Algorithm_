import math
while(1):
    [a,b,c] = map(int,input().split())
    array = sorted([a,b,c])
    if a==0 and b==0 and c==0:
        break
    if (math.pow(array[0],2) + math.pow(array[1],2)) == math.pow(array[2],2):
        print("right")
    else:
        print("wrong")