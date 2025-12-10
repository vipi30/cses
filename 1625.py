import sys

def solve(r, c, step):
    #si ya estamos en el obj.
    if r == 7 and c == 1:
        if step == 48: 
            return 1 
        return 0
    
    #Si ya hemos dado 48 pasos y no estamos en la meta, ha fallado
    if step == 48:
        return 0
    
    if visited[r-1][c] and visited[r+1][c] and not visited[r][c-1] and not visited[r][c+1]:
        return 0
    
    if visited[r][c-1] and visited[r][c+1] and not visited[r-1][c] and not visited[r+1][c]:
        return 0

    # Decidir movimiento según el input
    count = 0
    current_char = path_desc[step]
    #rango 4 porque estamos probando todas las direcciones posibles.
    for i in range(4):
        if current_char != '?' and current_char != chars[i]:
            continue
        nr, nc = r + dr[i], c + dc[i]
        
        if not visited[nr][nc]:
            visited[nr][nc] = True
            count += solve(nr, nc, step + 1)
            visited[nr][nc] = False 
            
    return count

sys.setrecursionlimit(5000) #para que no se vuelva loco

path_desc = sys.stdin.read().strip() #el .strip() es para quitar lo que sobra de una cadena de texto (como saltos de línea por ejemplo)

visited = [[False] * 9 for _ in range(9)]

#esto es para marcar todos los bordes como si ya hubiesen sido visitados.
for i in range(9):
    visited[0][i] = True
    visited[8][i] = True
    visited[i][0] = True
    visited[i][8] = True

visited[1][1] = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
chars = ['U', 'D', 'L', 'R']

print(solve(1, 1, 0))
