import sys 

read = sys.stdin.read().split()
n = int(read[0])
x = read[1:]

rounds = 1
posicion = [0] * (n+1)
for i in range(n): 
    valor = int(x[i])
    posicion[valor] = i

for j in range(2, n+1): 
    if posicion[j] < posicion[j-1]: 
        rounds += 1
sys.stdout.write(str(rounds))


