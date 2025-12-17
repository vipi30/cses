import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))
x = int(next(read))

p = [int(next(read)) for _ in range(n)]
p.sort() 

i = 0
j = n-1
gondola = 0

while i <= j: #i apunta al más ligero y j al más pesado
    if p[i] + p[j] <= x: #en el caso de que puedan ir juntos el más pesado y el menos.
        i+=1
        j-=1
    else: #sino, el peso aumenta.
        j-=1 
    gondola += 1 

print(gondola)
