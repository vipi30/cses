import sys

read = sys.stdin.read().split()
n = int(read[0])
a = list(map(int, read[1:]))

c = [0] * n
c[0] = 1
suma = 0
res = 0

for numero in a: 
    suma += numero 
    resto = suma % n 
    res += c[resto]
    
    c[resto] += 1 

print(res)
