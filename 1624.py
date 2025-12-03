def backtrack(fila):
    if fila == 8:
        return 1 #se ha encontrado una solución.

    suma = 0 
    for col in range(8): 
        if tablero[fila][col] == '*': 
            continue 
        if c_usadas[col]: 
            continue

        d1 = fila - col + 7
        if d1_usadas[d1]: 
            continue 

        d2 = fila + col 
        if d2_usadas[d2]: 
            continue 
        
        #si todo lo anterior, entonces la casilla es válida y podemos colocar a la reina.
        c_usadas[col] = True 
        d1_usadas[d1] = True 
        d2_usadas[d2] = True 

        suma += backtrack(fila + 1) 

        #aquí sucede el backtracking, porque deshace toda la colocación.
        c_usadas[col] = False 
        d1_usadas[d1] = False 
        d2_usadas[d2] = False 

    return suma


tablero = [input().strip() for _ in range(8)]

c_usadas = [False] * 8 
d1_usadas = [False] * 15
d2_usadas = [False] * 15 

print(backtrack(0)) #0 porque es la fila por la que quiero que empiece a resolver el problema. Es por donde intentará ir colocando a las reinas en el tablero.
