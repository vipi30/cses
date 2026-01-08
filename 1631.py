import sys

read = sys.stdin.read().split()
n = int(read[0])
t = list(map(int, read[1:]))

suma = sum(t)
max_libro = max(t)
print(max(suma, 2*max_libro))
