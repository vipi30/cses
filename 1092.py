def main(): 
    n = int(input())

    total = n * (n + 1) //2 
    if total%2 !=0: 
        print('NO')
        return 

    print('YES')

    target = total //2 
    set1 = []
    used = [False] * (n+1)

    for x in range(n, 0, -1):
        if x <= target: 
            set1.append(x)
            used[x] = True
            target -= x 
    
    set2 = []
    for x in range(1, n+1): 
        if not used[x]: 
            set2.append(x)

    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)

if __name__ == '__main__': 
    main()
