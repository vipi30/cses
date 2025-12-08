q = int(input())

for _ in range(q):
    k = int(input())
    l = 1          
    cantidad = 9           
    
    while k > l * cantidad:
        k -= l * cantidad 
        l += 1          
        cantidad *= 10          

    start = 10**(l-1)
    objetivo = start + (k-1) // l 
    indice = (k-1) % l
    
print(str(objetivo)[indice])
