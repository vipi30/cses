import sys 
from collections import deque 

read = sys.stdin.read().split()
n = int(read[0])

ch = deque(range(1, n+1)) #n+1 porque sino solo llega hasta n-1
salida = [] 
#saltamos el primer número, lo pasamos al final y eliminamos al siguiente.
#mientras aún haya algo en la cola: 
while ch: 
    #primero lo saltamos
    ch.rotate(-1)
    #luego eliminamos:
    e = ch.popleft()
    salida.append(e)
#sys.stdout.write(' '.join(str(salida)))
print(*salida)

