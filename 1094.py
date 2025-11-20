import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))
x = [int(next(read)) for _ in range(n)]

pasos = 0
for i in range(1, len(x)):
    if x[i] < x[i-1]: 
        pasos += x[i-1] - x[i]
        x[i] = x[i-1]
print(pasos)
