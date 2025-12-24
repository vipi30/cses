import sys 

read = sys.stdin.read().split()
n = read[0]
coins = sorted(map(int, read[1:]))

suma = 1 
for coin in coins: 
    if coin <= suma:
        suma += coin 
print(suma)
