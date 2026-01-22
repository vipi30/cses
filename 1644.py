import sys 
from collections import deque 

read = sys.stdin.read().split()
n = int(read[0])
a = int(read[1])
b = int(read[2])
x = list(map(int, read[3:]))

prefijo = [0] * (n+1)
for i in range(n): 
    prefijo[i+1] = prefijo[i] + x[i]
    
cola = deque()
maximo = -float('inf')

for j in range(a, n+1): 
    nuevo = j-a 
    while cola and prefijo[cola[-1]] >= prefijo[nuevo]: 
        cola.pop() 
    cola.append(nuevo)

    if cola[0] < j-b: 
        cola.popleft() 

    suma = prefijo[j] - prefijo[cola[0]]
    if suma > maximo: 
        maximo = suma 
print(maximo)

