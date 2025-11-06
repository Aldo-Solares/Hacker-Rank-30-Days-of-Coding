
#LINK https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true

import sys

my_dict = {}
n = int(input())

for x in range(n):
    k,v = input().split()
    my_dict.update({k:v})

try:
    while True:
        name = input()
        if my_dict.get(name):
            print(f"{name}={my_dict.get(name)}")
        else:
            print("Not found")
except Exception as e:
    pass
