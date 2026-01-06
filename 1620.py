#búsqueda binaria
import sys 

read = sys.stdin.read().split()
n = int(read[0]) #numero de maquinas
t = int(read[1]) #tiempo necesario para producir
k = list(map(int, read[2:])) #tiempo por máquina

minimo = 1
maximo = 10**18
res = maximo 

while minimo <= maximo: 
    mitad = (minimo+maximo) // 2 #cuantos productos se hacen en este tiempo
    total = 0
    for maquina in k: 
        total += mitad // maquina
        if total >= t: #si ya llegamos al tiempo t, no hace falta seguir
            break 
    
    if total >= t: 
        res = mitad 
        maximo = mitad - 1

    else: #se necesita más tiempo  
        minimo = mitad + 1

print(res)
