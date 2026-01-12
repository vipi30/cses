import sys

read = sys.stdin.read().split()
n = int(read[0])
x = int(read[1])
a = list(map(int, read[2:]))

#dos punteros 
c = 0
izquierda = 0

suma_actual = 0
for i in range(n): 
    suma_actual += a[i]

    while suma_actual > x and izquierda <= i: 
        suma_actual -= a[izquierda]
        izquierda+= 1

    if suma_actual == x: 
        c += 1
print(c)

