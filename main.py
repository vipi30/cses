n = int(input())

salida = [n]
while n != 1: 
    if n % 2 == 0: 
        n = n // 2
    else: 
        n = n*3 + 1
    salida.append(n)
print(*salida) 
    

