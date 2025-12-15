import sys 
read = iter(sys.stdin.read().split())
n = next(read)
dv = set(read)
print(len(dv))
