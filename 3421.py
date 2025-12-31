#una subsecuancia es cuantos cubconjuntos puedo hacer del conjunto inicial pero manteniendo su orden original (podiéndome saltar elementos) y con elementos distintos.
#usamos la combinatoria (variación sin repetición)
import sys 
from collections import Counter #sirve para saber cuántas veces aparece cada número.

read = sys.stdin.read().split()
n = int(read[0])
x = read[1:]

cuenta = Counter(x) 
res = 1

#pide printearlo en modulo 10^9 + 7 porque pueden haber resultados muy grandes.
modulo = 10**9 + 7 
for c in cuenta.values(): #c va a ser cuántas veces aparece cada número, no cada número.
    #vamos multiplicando
    res = (res * (int(c)+1)) % modulo
print((res - 1 + modulo) % modulo)
