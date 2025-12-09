l = input() 
#hay que tener en cuenta que hay que reordenar las letras de forma en la que me tengo que asegurar de que que las letras que aún quedan se pueden colocar sin repetirse dos veces seguidas.

#lo de las frecuencias es importante porque hay que pensar en casos en los que es imposible colocar las letras sin que se toquen. 

#creo el array para las frecuencias. 
contar = [0] * 26
for letras in l: 
    contar[ord(letras)-65] += 1 #ord era lo de los números asociados a cada caracter. 65 es el asociado a la letra 'A', la que estariamos colocando en el índice 0. 

limite = (len(l)) // 2 #-> para asegurar que no estamos ante un caso imposible.

if max(contar) > limite: 
    print(-1) 
    exit #para que no siga ejecutando el resto.

ans = [] 
ultimo = -1 

for i in range(len(l)): 
    resto = len(l)-1-i 
    limite = (resto+1) // 2 
    
    posible = False 

    for ch in range(26): 
        if contar[ch] == 0: 
            continue 

        if ch == ultimo: #si el caracter actual es igual al anterior.
            continue 

        contar[ch] -= 1 

        if max(contar) <= limite: 
            ans.append(chr(ch + 65)) 
            ultimo = ch 
            posible = True #ahora si es una posibilidad la forma de colocarlo. 
            break 
        else: 
            contar[ch] += 1 

    if not posible: #si posible sigue siendo falso
        print(-1)
        exit 

print(''.join(ans))
