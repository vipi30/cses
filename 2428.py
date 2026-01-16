import sys

read = sys.stdin.read().split()
n = int(read[0])
k = int(read[1])
x = read[2:]

izq = 0
res = 0
d = 0
diccionario = {} 

for i in range(n):
    actual = x[i]
    if diccionario.get(actual, 0) == 0: 
        d += 1
        diccionario[actual] = 1
    else: 
        diccionario[actual] += 1
    
    while d > k: 
        valor = x[izq]
        diccionario[valor] -= 1
        if diccionario[valor] == 0: 
            d -= 1
        izq += 1
    
    res += (i-izq+1)
print(res)
