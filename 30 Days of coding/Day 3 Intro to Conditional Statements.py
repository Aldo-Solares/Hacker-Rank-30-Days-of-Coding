
#LINK https://www.hackerrank.com/challenges/30-conditional-statements/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input().strip())
    if N%2 == 0:
        if N<=5 and N>=2:
            print("Not Weird")
        elif N>20:
            print("Not Weird")
        else:
            print("Weird")
    else:
        print("Weird")
