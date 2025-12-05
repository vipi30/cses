n = int(input())

a = [[0] * n for _ in range(n)] #-> formando una matriz llena de ceros.

#mex -> minimum excluded 
#cómo calcular el mex para cada casilla:
for i in range(n): 
    for j in range(n):
        seen = [False] * (2 * n + 5) #-> array de booleanos para que indique qué valores han aparecido ya. Usa 2n+5 porque el mex nunca pasa de 2n. 
        
        #esto para recorrer las casillas a la izquierda en la misma fila.
        for k in range(j): 
            seen[a[i][k]] = True #-> marca como true los valores que ya aparecieron en esa fila antes de la columna.

        for k in range(i): 
            seen[a[k][j]] = True 

        x = 0 
        while seen[x]: 
            x += 1 #calcula el mex, que es el numero más pequeño que no aparece ni a la izquierda ni arriba.

        a[i][j] = x #-> asigna el mex a la posición actual

salida = [] 
for i in range(n): 
    salida.append(' '.join(str(x) for x in a[i]))

for filas in salida: 
    print(filas)

