import sys

read = sys.stdin.read().split()
n = int(read[0])
p = sorted(map(int, read[1:]))
 
mediana = p[n//2]

suma = 0
for x in p: 
    suma += abs(x-mediana)
sys.stdout.write(str(suma))
