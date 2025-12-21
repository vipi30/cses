import sys 

def solve():
    read = sys.stdin.read().split()
    n = int(read[0])
    x = int(read[1])

    a = map(int, sys.stdin.read().split())

    vistos = {}
    for i in range(n):
        actual = int(read[i+2])
        objetivo = x-actual
        if objetivo in vistos: 
            print(vistos[objetivo], i+1)
            sys.exit()
        vistos[actual] = i+1
    
    print('IMPOSSIBLE')
solve()
