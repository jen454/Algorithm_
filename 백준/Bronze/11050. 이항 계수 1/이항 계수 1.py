N,K = map(int,input().split())
def factorial(num):
    sum = 1
    for i in range(2,num+1):
        sum *= i
    return sum
print(factorial(N) // (factorial(N-K) * factorial(K)))