
#LINK https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true

import re
if __name__ == '__main__':
    n = int(input().strip())
    texto_num = bin(n)[2:]
    print(texto_num)
    matches = re.findall(r"1+",texto_num)
    if matches:
        matches.sort(reverse=True)
        print(matches[0])