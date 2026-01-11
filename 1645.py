import sys

read = sys.stdin.read().split()
n = int(read[0])
x = list(map(int, read[1:]))

res = []
pila = []
for i in range(n): 
    act = x[i]
    pos = i+1

    while pila and pila[-1][0] >= act: 
        pila.pop() 
    
    #si está vacío
    if not pila: 
        res.append(0)
    else: 
        res.append(pila[-1][1])

    pila.append((act, pos))
print(*res)




