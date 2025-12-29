#linked list -> es una lista que tiene dos partes, el dato en sí y un puntero que apunta al siguiente elemento.  
#usamos double linked list (dll) -> es como si tuviera tres partes, el valor en sí y dos punteros, uno señalando al siguiente elemento y otro al anterior.
import sys 

read = sys.stdin.read().split()
x =int(read[0])
n = int(read[1])
p = list(map(int, read[2:]))

#la dll se simula con un diccionario porque no hay una estructura como tal.

lista_ordenada = sorted([0, x]+p) #para establecer las conexiones iniciales.
m = len(lista_ordenada)
posicion = {val: i for i, val in enumerate(lista_ordenada)} #aquí estoy creando un diccionario en el que pongo que el key sea el valor del semáforo y el value sea su posición en la lista.

left = [i - 1 for i in range(m)]
right = [i + 1 for i in range(m)]

res = []
maximo_espacio = 0 

for i in range(1, m): 
    maximo_espacio = max(maximo_espacio, lista_ordenada[i]-lista_ordenada[i-1])

for i in range(n-1, -1, -1):  #porque estamos yendo de atrás hacia delante.
    res.append(maximo_espacio)
    quitar = p[i]
    indice = posicion[quitar]

    i_left = left[indice]
    i_right = right[indice]
    nuevo_espacio = lista_ordenada[i_right] - lista_ordenada[i_left]
    maximo_espacio = max(nuevo_espacio, maximo_espacio)

    if i_right < m: 
        left[i_right] = i_left 
    if i_left >= 0: 
        right[i_left] = i_right 

print(*(res[::-1])) #le damos la vuelta porque lo hicimos al revés

