n = int(input())
a = list(map(int, input().split()))

lista = []
for i in range(n): 
    if a[i] not in lista: 
        lista.append(a[i])
print(len(lista))
