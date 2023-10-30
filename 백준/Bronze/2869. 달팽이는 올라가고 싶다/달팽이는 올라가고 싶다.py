# 2 1 3 2 4 3 5 4
# 5 4 9 5
# 100 1 101 2 102 3
A,B,V = map(int,input().split())
result = (V-B)/(A-B)
if result == int(result):
    print(int(result))
else:
    print(int(result)+1)