#un rango [a, b] contiene a otro [c, d] si a<=c y d<=b
import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))

rangos = []

for i in range(n): 
    x = int(next(read))
    y = int(next(read))
    rangos.append([x,y,i])

#ordeno los rangos de forma en la que ya se cumpla que a<=c
rangos.sort(key=lambda x: (x[0], -x[1])) 

contiene = [0] * n #aquí guardo si contiene a otro rango
contenido = [0] * n #aquí guardo si es contenido por otro rango

max_final = 0
min_final = float('inf')
for x,y,i in rangos: 
    if y <= max_final:
        contiene[i] = 1
    max_final = max(y, max_final)
for x,y,i in reversed(rangos): 
    if y>= min_final:
        contenido[i] = 1
    min_final = min(y, min_final)

print(*contenido)
print(*contiene)

    
