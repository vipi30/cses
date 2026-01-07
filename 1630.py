#greedy 
#recompensa = (d1−f1)+(d2−f2)+(d3−f3)
#Recompensatotal =(d1+d2+d3)−(f1+f2+f3)
import sys

read = sys.stdin.read().split() 
n = int(read[0])

tareas = [] 

indice = 1 
for i in range(n): 
    a = int(read[indice])
    d = int(read[indice+1])
    tareas.append((a,d))
    indice+=2

tareas = sorted(tareas)

recompensa = 0
tiempo = 0
for duracion, limite in tareas: 
    tiempo += duracion #vamos contando el tiempo que tarda cada tarea. 
    recompensa += (limite-tiempo)
print(recompensa)
