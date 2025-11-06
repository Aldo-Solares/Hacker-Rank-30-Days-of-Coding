
#LINK https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    counter = 0
    
    pre_a = a[:]
    
    while sorted(a) != a:
        for x in range(len(a)-1):
            if a[x] > a[x+1]:
                pre_a[x], pre_a[x+1] = pre_a[x+1], pre_a[x]
                counter += 1
        a = pre_a[:]
        
    print(f"Array is sorted in {counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")