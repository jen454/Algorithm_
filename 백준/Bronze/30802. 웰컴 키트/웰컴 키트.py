import math

N = int(input()) # 참가자의 수
size = list(map(int,input().split())) # 사이즈별 신청자 수
T, P = map(int,input().split()) # T: 티셔츠 묶음 수 P: 펜의 묶음 수
group_T = 0 # 티셔츠 T장씩 최소 묶음 주문 수
for i in range(len(size)):
    group_T += math.ceil(size[i] / T)
print(group_T)
print(N // P, N % P)