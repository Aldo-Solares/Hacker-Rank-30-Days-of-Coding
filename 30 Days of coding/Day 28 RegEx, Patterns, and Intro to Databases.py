
#LINK https://www.hackerrank.com/challenges/30-regex-patterns/problem?isFullScreen=true

import re

if __name__ == '__main__':
    N = int(input().strip())
    
    name_list = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        matches = re.search("@gmail.com",emailID)
        
        if matches:
            
            name_list.append(firstName)
    
    name_list.sort()
    
    print("\n".join(map(str, name_list)))
