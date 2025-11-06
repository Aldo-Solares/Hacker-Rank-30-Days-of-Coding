
#LINK https://www.hackerrank.com/challenges/30-arrays/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])