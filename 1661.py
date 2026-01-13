import sys

read = sys.stdin.read().split()
n = int(read[0])
x = int(read[1])
a = map(int, read[2:])

#dos punteros 
c = {0:1}
suma = 0
res = 0

for numero in a: 
    suma += numero
    target = suma - x

    if target in c: 
        res += c[target]

    c[suma] = c.get(suma, 0) + 1

print(res)
