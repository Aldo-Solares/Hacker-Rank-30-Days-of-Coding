
#LINK https://www.hackerrank.com/challenges/30-bitwise-and/problem?isFullScreen=true

#Note My solution
from itertools import combinations

def bitwiseAnd(N, K):
    numbers = list(range(1, N+1))
    combinatios = list(combinations(numbers,2))
    
    combinatios = [(A & B) for (A,B) in combinatios if (A & B) <K]

    return max(combinatios)


#Nota The solution I found
def bitwiseAnd(N, K):
    return K-1 if ((K-1) | K) <= N else K-2

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        print(res)