import sys

read = sys.stdin.read().split()
n = int(read[0])
x = int(read[1])
a = list(map(int, read[2:]))

numeros = []
for i in range(n): 
    numeros.append((a[i], i+1))

numeros.sort()

for i in range(n): 
    valor_a, indice = numeros[i]
    b = x - valor_a
    
    izq = i + 1
    drc = n - 1
    while izq < drc: 
        suma = numeros[izq][0] + numeros[drc][0]

        if suma == b: 
            print(f'{indice} {numeros[izq][1]} {numeros[drc][1]}')
            sys.exit()

        if suma < b: 
            izq += 1 
        else:
            drc -= 1 

print('IMPOSSIBLE')
