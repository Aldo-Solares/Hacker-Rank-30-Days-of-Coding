
#LINK https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

for x in range(int(input())):
    letras_listas = list(input())
    palabra_1 = ""
    palabra_2 = ""
    
    for y in range(0,len(letras_listas), 2):
        palabra_1 += letras_listas[y]
    
    for y in range(1,len(letras_listas), 2):
        palabra_2 += letras_listas[y]
        
    print(palabra_1, palabra_2)
