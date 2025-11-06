
#LINK https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true

def is_prime(number):
    if number <= 1:
        print("Not prime")
        return
    if number <= 3:
        print("Prime")
        return
    if number % 2 == 0 or number % 3 == 0:
        print("Not prime")
        return
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            print("Not prime")
            return
        i += 6
    print("Prime")

n = int(input())
for _ in range(n):
    number = int(input())
    is_prime(number)
