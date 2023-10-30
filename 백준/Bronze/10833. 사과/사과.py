N = int(input())
sum = 0
for i in range(N):
    A,B = map(int,input().split())
    sum += B%A
print(sum)