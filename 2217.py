import sys 

read = sys.stdin.read().split() 
n = int(read[0])
m = int(read[1])

a = [0] * (n+1)
posicion = [0] * (n+2)

for i in range(1, n+1): 
    valor = int(read[i+1])
    a[i] = valor 
    posicion[valor] = i 

rondas = 1
for i in range(2, n+1): 
    if posicion[i] < posicion[i-1]: 
        rondas += 1

indice = n+2 
res = []

for j in range(m):
    pos_a = int(read[indice])
    pos_b = int(read[indice+1])
    indice += 2

    val_a = a[pos_a]
    val_b = a[pos_b]
    
    afectados = set() #creo el set con un conjunto de pares para que no se repitan. El punto es identificar los pares afectados.
    if val_a > 1: 
        afectados.add(val_a - 1)
    if val_a < n: 
        afectados.add(val_a)
    if val_b > 1: 
        afectados.add(val_b - 1)
    if val_b < n: 
        afectados.add(val_b)
    
    for i in afectados:
        if posicion[i] > posicion[i+1]:
            rondas -= 1

    #cambio de posiciones 
    a[pos_a], a[pos_b] = val_b, val_a
    posicion[val_a], posicion[val_b] = pos_b, pos_a
    
    for i in afectados:
        if posicion[i] > posicion[i+1]:
            rondas += 1
            
    res.append(str(rondas))
sys.stdout.write("\n".join(res))
