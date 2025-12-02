def dfs(i, sumA):
    global best #para indicar que es la misma variable que está fuera de la función.
    #sumA = suma del grupo 1.
    #sumB = total - sumA -> para el grupo de manzanas 2.
    if i == n:
        diferencia = abs(total - 2 * sumA)
        best = min(best, diferencia)
        return

    #primera opción: no cogemos a[i] para incluirlo en el grupo A
    dfs(i + 1, sumA)

    #segunda opción: sí incluimos a[i] en el grupo A
    dfs(i + 1, sumA + peso[i])


n = int(input())
peso = list(map(int, input().split()))

total = sum(peso) #calculamos la suma total de todos los pesos.
best = 10**18  #un número grande cualquiera.

dfs(0, 0)
print(best)

