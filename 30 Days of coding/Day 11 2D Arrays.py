
#LINK https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    max_sum = -63
    y = 0
    for x in range(len(arr[0])-2):
        for y in range(len(arr[0])-2):
            current_sum = (arr[x][y]+arr[x][y+1]+arr[x][y+2]+
                                     arr[x+1][y+1]+
                           arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2])
            if current_sum > max_sum:
                max_sum = current_sum
                
    print(max_sum)
