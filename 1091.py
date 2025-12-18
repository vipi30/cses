import sys 
from bisect import bisect_right 

read = iter(sys.stdin.read().split())
n = int(next(read))
m = int(next(read))

h = [int(next(read)) for _ in range(n)]
t = [int(next(read)) for _ in range(m)]

h.sort() 
parent = list(range(n))

def find(i): 
    if i < 0: 
        return -1
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i] 

res = []
for max_p in t: 
    idx = bisect_right(h, max_p)-1

    dis_idx = find(idx)
    
    if dis_idx != -1: 
        res.append(str(h[dis_idx])) 
        parent[dis_idx] = find(dis_idx-1)
    else: 
        res.append('-1')
print('\n'.join(res)+'\n')

