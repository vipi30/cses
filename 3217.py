from collections import deque #-> double ended queue.

n = int(input())
#a tener en cuenta -> pide movimientos DE CABALLO DE AJEDREZ (se mueve en L). 


dist = [[-1]*n for _ in range(n)]
movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

dist[0][0] = 0
cola = deque()
cola.append((0,0))

while cola: #mientras haya algo en cola.
    i, j = cola.popleft() 

    for di, dj in movimientos: 
        ni = i+di 
        nj = j+dj 

        if 0 <=  ni < n and 0 <= nj < n: #si está dentro del tablero.
            if dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                cola.append((ni, nj))
            #cola.append(nj)

for fila in dist:
    print(*fila)



