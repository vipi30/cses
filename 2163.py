import sys 

def buscarK(obj): 
    indice = 0
    for i in range(n.bit_length(), -1, -1): 
        sig = indice + (1 << i) 
        if sig <= n and bit[sig] < obj: 
            indice = sig 
            obj -= bit[indice]
    return indice+1

#función para actualizar el bit
def act(i, delta): 
    while i <= n: 
        bit[i] += delta
        i += i&(-i)
read = sys.stdin.read().split()
n = int(read[0])
k = int(read[1])

#fenwick tree en una lista
bit = [0] * (n+1)

for i in range(1, n+1): 
    act(i, 1)

salida = []
pos_actual = 0

for niños in range(n, 0, -1):
    pos_actual = (pos_actual+k) % niños
    i_real = buscarK(pos_actual+1)
    salida.append(str(i_real))
    act(i_real, -1)
print(*salida)

