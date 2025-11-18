t = int(input())
n = list(map(int, input().split()))

tot = t * (t + 1) // 2
print(tot-sum(n))
