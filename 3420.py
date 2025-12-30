import sys 

read = sys.stdin.read().split()
n = int(read[0])
x = read[1:]

#punteros hacia right y left
l = 0
total = 0
contador = {} #para almacenar cuántas veces aparece cada letra.

for r in range(n): 
    valor_r = x[r] 
    contador[valor_r] = contador.get(valor_r, 0)+1
    while contador[valor_r] > 1: 
        valor_l = x[l]
        contador[valor_l] -= 1
        l+=1
        
    total += (r-l+1) 
print(total)


