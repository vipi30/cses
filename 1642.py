import sys

read = sys.stdin.read().split()
n = int(read[0])
x = int(read[1])

a = [int(val) for val in read[2:]]
vistas = {}

for i in range(n): 
    for j in range(i+1, n): 
        c = x-(a[i] + a[j]) #meet in the middle
        if c in vistas: 
            p1, p2 = vistas[c]

            print(f'{p1} {p2} {i+1} {j+1}')
            exit()

    for k in range(i): #para q no se solapen
        par = a[k] + a[i]
        vistas[par] = (k+1, i+1)
print('IMPOSSIBLE')
