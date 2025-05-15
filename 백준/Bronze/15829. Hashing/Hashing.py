L = int(input())
S = input()
H = 0
for i in range(L):
    H += (ord(S[i])-96) * (31 ** i)
print(H % 1234567891)