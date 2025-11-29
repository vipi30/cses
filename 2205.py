n = int(input())

total = 1 << n  #<< y >> para desplazar los bits (bit shifts). Se desplazan hacia el lado que apunta la flecha.

for i in range(total):
    greyC = i ^ (i >> 1)          # así se calcula el número en Gray code
    s = format(greyC, f'0{n}b')   #de esta forma lo convierto al formato de los bits
    print(s)
