T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
    room = ((N-((N//H)*H))*100) + (N//H+1)
    if (N%H==0):
        room = (H*100) + (N//H)
    print(room)