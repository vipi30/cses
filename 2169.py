import sys
def solve():
    #fewick tree
    def act(bit, indice, val):
        while indice <= max_rango:
            bit[indice] += val
            indice += indice & (-indice)

    def query(bit, indice):
        s = 0
        while indice > 0:
            s += bit[indice]
            indice -= indice & (-indice)
        return s

    read = sys.stdin.read().split()

    n = int(read[0])
    rangos = []
    c = set()
    
    i = 1
    for j in range(n):
        x = int(read[i])
        y = int(read[i+1])        
        rangos.append([x, y, j])
        c.add(y)
        i += 2

    c_ord = sorted(list(c))
    rango = {val: i + 1 for i, val in enumerate(c_ord)}
    max_rango = len(c_ord)

    contiene = [0] * n
    contenido = [0] * n
    rangos.sort(key=lambda r: (r[0], -r[1]))

    bit = [0] * (max_rango + 1)
    for x, y, i in rangos:
        r = rango[y]
        contenido[i] = query(bit, max_rango) - query(bit, r - 1)
        act(bit, r, 1)

    bit = [0] * (max_rango + 1)

    for x, y, i in reversed(rangos):
        r = rango[y]
        # Queremos y_next <= y_curr -> sumamos desde 1 hasta r
        contiene[i] = query(bit, r)
        act(bit, r, 1)

    print(*contiene)
    print(*contenido)

solve()
