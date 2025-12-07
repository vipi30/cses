import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))
m = int(next(read)) 

grid = [next(read) for _ in range(n)]

caracteres = ['A', 'B', 'C', 'D'] #-> los colores.

res = [['']*m for _ in range(n)] #constuyo la solución como una lista de listas.

for i in range(n): 
    for j in range(m): 
        forbidden = set() 

        forbidden.add(grid[i][j])
        #si hay arriba
        if i > 0: 
            forbidden.add(res[i - 1][j])
        #si hay izquierda
        if j > 0:
            forbidden.add(res[i][j - 1])

        for ch in caracteres:
            if ch not in forbidden:
                res[i][j] = ch
                break
            #no hace falta poner lo de imprimir impossible porque siempre se puede.

salida = [] 
for i in range(n):
    salida.append(''.join(res[i]))
print('\n'.join(salida))

