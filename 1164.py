import sys
import heapq

read = sys.stdin.read().split()
n = int(read[0])

c = []
p = 1

for i in range(n): 
    llegadas = int(read[p])
    salidas = int(read[p+1])
    c.append((llegadas, salidas, i))
    p += 2

c.sort()

cuartos = []
a = [0] * n
suma = 0

for llegadas, salidas, i in c: 
    if cuartos and cuartos[0][0] < llegadas: #si hay habs libres
        _, id_c = heapq.heappop(cuartos)
    else: 
        suma += 1 
        id_c = suma 
    a[i] = id_c 
    heapq.heappush(cuartos, (salidas, id_c))
print(suma)
print(*a)

