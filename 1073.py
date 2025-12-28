#búsqueda binaria -> bisect 
#bisect_right busca el lugar donde x debería ir para mantener el orden, dandole la posiciones del primer elemento que es estrictamente mayor que x. 
import sys 
from bisect import bisect_right 

read = sys.stdin.read().split()
n = int(read[0])
cubos = map(int,read[1:])

torres = []

for cubo in cubos: 
    i = bisect_right(torres, cubo)
    if i < len(torres): 
        torres[i] = cubo
    else: 
        torres.append(cubo)
print(len(torres))
