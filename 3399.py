import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

salida = []
for _ in range(t): 
    n = int(next(read))
    a = int(next(read))
    b = int(next(read))
    
    # casos imposibles
    if a + b > n or (min(a, b) == 0 and max(a, b) != 0): 
        salida.append('NO')
        continue

    salida.append('YES')

    # jugador 1: 1..n
    fila1 = [] 
    for i in range(1, n + 1): 
        fila1.append(str(i))
    salida.append(' '.join(fila1))

    # jugador 2
    if a == 0 and b == 0: 
        fila2 = ' '.join(fila1)
    else: 
        m = a + b 
        arr = list(range(a + 1, m + 1)) + list(range(1, a + 1))
        # turnos restantes: empates (i vs i)
        if m < n:
            arr += list(range(m + 1, n + 1))
        fila2 = " ".join(str(x) for x in arr)

    salida.append(fila2)

sys.stdout.write("\n".join(salida))

