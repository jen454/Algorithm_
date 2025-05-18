# 어떠한 경우에도 fizz, buzz, fizzbuzz가 한번에 다 나오진 않는다.
# 숫자를 찾아내서 입력 다음으로 올 숫자를 유추할 수 있다.

def is_fizz_buzz(num):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

fb = ['Fizz', 'Buzz', 'FizzBuzz'] # fizzbuzz 문자 배열
next = 0 # 다음으로 올 숫자
for i in range(3):
    num = input()
    if (num not in fb):
        next = int(num) + (3-i)

is_fizz_buzz(next)