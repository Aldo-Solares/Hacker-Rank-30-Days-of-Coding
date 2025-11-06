
#LINK https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true

S = input()

try:
    print(int(S))
except ValueError:
    print("Bad String")