import sys 
def solve():
    read = sys.stdin.read().split()
    n = int(read[0])
#para obtener las entradas y las salidas
    llegadas = sorted(map(int, read[1::2])) 
    salidas = sorted(map(int, read[2::2]))

    max_clientes= 0
    actuales = 0
    #creo dos punteros hacia las llegas y las salidas
    i=0
    j=0 

    while i < n: 
        if llegadas[i] < salidas[j]: 
            actuales += 1
            if actuales > max_clientes:
                max_clientes = actuales 
            i+=1
        else: #para cuando se va alguien
            actuales -= 1
            j+=1 
    sys.stdout.write(str(max_clientes))

solve()



