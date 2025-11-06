
#LINK https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true

class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        max_num = max(self.__elements)
        min_num = min(self.__elements)
        difference = abs(max_num - min_num)

        self.maximumDifference = difference
        
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)