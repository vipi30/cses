import sys 

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t): 
    a = int(next(read))
    b = int(next(read))
    c = a + b 
    if c % 3 == 0 and 2 * min(a,b) >= max(a, b): 
        print('YES')
    else: 
        print('NO')
