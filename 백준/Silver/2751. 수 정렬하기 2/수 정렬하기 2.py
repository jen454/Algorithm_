import sys
N = int(input())
List = []
for i in range(N):
    List.append(int(sys.stdin.readline()))
for i in sorted(List):
    print(i)