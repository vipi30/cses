import sys

read = sys.stdin.read().split()
n = int(read[0])
r_movies = read[1:]

movies = []
for i in range(0, 2 * n, 2): 
    movies.append((int(r_movies[i]), int(r_movies[i+1])))

# toma el elemento x y me devuelve todo loq ue haya en la posición 1. Esto es que  si las películas son una lista de pares, coge de los pares el segundo número.
movies.sort(key=lambda x: x[1]) 

count = 0
ultima_hora = 0 

for principio, fin in movies: 
    if principio >= ultima_hora: 
        count += 1
        ultima_hora = fin
print(count)
