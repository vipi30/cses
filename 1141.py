import sys 

read = sys.stdin.read().split()
n = int(read[0])
canciones = read[1:]

#usamos dos punteros.
#creamos un diccionario para guardar la posicion de cada cancion. 
posiciones = {}
i = 0 #apuntando a la izquierda
ans = 0 

for j in range(n): #este es el segundo puntero, j va cancion por cancion
    c = canciones[j]
    if c in posiciones and posiciones[c] >= i: 
        i = posiciones[c]+1

    posiciones[c] = j 
    tamaño_actual = j-i+1
    if tamaño_actual > ans: 
        ans = tamaño_actual

sys.stdout.write(str(ans))
        



