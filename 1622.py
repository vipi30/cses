from collections import Counter 
import math

def backtrack(prefijo):
    if len(prefijo) == n: 
        print(''.join(prefijo))
        return
    for c in caracteres: #para probar una por una que letra puede ir en la siguiente posición. 
        if contar[c] > 0: #si aún quedan letras
            contar[c] -= 1
            prefijo.append(c)
            backtrack(prefijo)
            prefijo.pop() #para quitar la letra que acabo de probar.
            contar[c] += 1 #la devuelvo.

s = input().strip()
n = len(s)
strings = math.factorial(n) 

contar = Counter(s)
caracteres = sorted(contar.keys()) #counter donde las keys son las letras del string.

for i in contar.values(): #-> values es cuantas veces aparece cada letra.
    strings = strings//math.factorial(i)
print(strings) #ya tengo la cantidad de strings que puedo hacer. []

backtrack([])






