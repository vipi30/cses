n = int(input())

modulo = 10**9 + 7 

res = 1
for i in range(n):  
    res = (res * 2) % modulo 

print(res)
