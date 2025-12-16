import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))
m = int(next(read))
k = int(next(read))

a = [int(next(read)) for _ in range(n)]
b = [int(next(read)) for _ in range(m)]
a.sort() #lo hago por si hay más de uno en el que la diferencia del tamaño sea menor o igual que k
b.sort() 

#punteros como los que me explicó cuxiduxi
i = 0
j = 0
cuadran = 0

while i < n and j < m: 
    p = a[i]
    tamaño = b[j]
    if tamaño < p - k:
        j += 1

    elif tamaño > p + k: 
        i += 1

    else: 
        i += 1 
        j += 1
        cuadran += 1
print(cuadran) 

