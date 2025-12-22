import sys

#objetivo: elegir un segmento que me da la mayor suma posible, imprimir la suma

read = sys.stdin.read().split() #me tengo que acordar de dejar de poner iter, eso servía con el next(read).
n = int(read[0]) 
x = map(int, read[1:])
#pongo valores MUY pequeños para lidiar con arrays de negativos. 
mejor = -10**10 
racha = -10**10 
#si la racha que tengo acumulada es negativa empiezo desde cero
for numero in x: 
    #aquí aplico Kadane. 
    racha = max(numero, racha+numero)
    if racha > mejor: 
        mejor = racha 
print(mejor)
