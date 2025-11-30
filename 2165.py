n = int(input())

# La cantidad mínima de movimientos de las Torres de Hanoi es 2^n - 1
total = 2**n - 1
print(total)

def hanoi(dis, source, obj, aux):
    if dis == 1:
        print(source, obj)
        return

    hanoi(dis - 1, source, aux, obj)
    print(source, obj)
    hanoi(dis - 1, aux, obj, source)

hanoi(n, 1, 3, 2)
