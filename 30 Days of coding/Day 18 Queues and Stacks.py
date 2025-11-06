
#LINK https://www.hackerrank.com/challenges/30-queues-stacks/problem?isFullScreen=true

import sys
class Solution:
    stack = []
    cantidad = 2
    
    @classmethod
    def pushCharacter(cls, s):
        cls.stack.append(s)
        
    @classmethod    
    def enqueueCharacter(cls, s):
        cls.queue.append(s)
        
    @staticmethod  
    def popCharacter(cls):
        return cls.stack.pop(-1)
        
    @classmethod
    def dequeueCharacter(cls):
        return cls.queue.pop(0)
        
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    