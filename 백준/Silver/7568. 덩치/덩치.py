N = int(input())
A = [0 for i in range(N)]
B = []
for i in range(N):
    x,y = map(int,input().split())
    B.append([x,y])
for i in range(N):
    for j in range(i,N):
        if ((B[i][0] < B[j][0]) and (B[i][1] > B[j][1])) or ((B[i][0] > B[j][0]) and (B[i][1] < B[j][1])):
            continue
        elif (B[i][0] < B[j][0]) and (B[i][1] < B[j][1]):
            A[i] += 1
        elif ((B[i][0] > B[j][0]) and (B[i][1] > B[j][1])):
            A[j] += 1
for i in range(N):
    print(A[i]+1,end=" ")