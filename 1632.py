#fenwick tree and binary search
import sys 

def actualizar(i, delta, m, bit): 
    while i <= m: 
        bit[i] += delta
        i += i&(-i)

def query(i, bit): 
    s = 0
    while i > 0: 
        s+= bit[i]
        i -= i&(-i) 
    return s 

def buscar(v, m, bit, bit_len): 
    posicion = 0
    suma = 0
    for i in range(bit_len -1, -1, -1): 
        siguiente = posicion + (1 << i)
        if siguiente <= m and suma + bit[siguiente] < v: 
            posicion = siguiente 
            suma += bit[posicion]
    return posicion+1


read = iter(sys.stdin.read().split())
n = int(next(read))
k = int(next(read))

p = []
coor = {0}

for i in range(n): 
    empieza = int(next(read))
    acaba = int(next(read)) 
    p.append((empieza, acaba))
    coor.add(empieza)
    coor.add(acaba)

    ordenado = sorted(list(coor))
    r = {val: i+1 for i, val in enumerate(ordenado)}
    m = len(ordenado)
    bit = [0] * (m+1) #fenwick tree
    bit_len = m.bit_length()

    actualizar(r[0], k, m, bit)
    p.sort(key=lambda x: x[1])

    total = 0
    
    for s, e in p: 
        i_s = r[s]
        i_e = r[e]
        d = query(i_s, bit)
        
        if d > 0: 
            posicion = buscar(d, m, bit, bit_len)
            actualizar(posicion, -1, m, bit)
            actualizar(i_e, 1, m, bit)
            total += 1

print(total)

