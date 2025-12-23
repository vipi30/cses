import sys 

def solve():
    read = sys.stdin.read().split()
    n = int(read[0])
    x = int(read[1])

    a = [] 
    for i in range(n): 
        valor = int(read[i+2])
        a.append((valor, i+1)) #porque queremos que empiece a contar desde el 1 y no desde el 0.
    a.sort()
    
    i = 0
    j = n-1 

    while i < j: 
        suma = a[i][0] + a[j][0]
        if suma == x: 
            print(a[i][1], a[j][1])
            exit()
        if suma < x: 
            i += 1 
        else: 
            j -= 1
    print('IMPOSSIBLE')
solve()

