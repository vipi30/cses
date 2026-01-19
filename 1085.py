import sys 

def puedo(m): 
    sub = 1 
    suma = 0
    for numero in x: 
        if suma + numero <= m: 
            suma += numero
        else: 
            sub+=1 
            suma = numero
    return sub<=k

read = sys.stdin.read().split() 
n = int(read[0])
k = int(read[1])
x = list(map(int, read[2:]))

b = max(x)
a = sum(x)
res = 0

while b <= a: 
    m = (b+a) // 2
    if puedo(m): 
        res = m
        a = m-1
    else: 
        b = m+1 
print(res)

