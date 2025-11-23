n = int(input())

for i in range(1, n+1): 
    t = ((i*i)*((i*i)-1)) // 2
    att = 4 * (i-1) * (i-2)
    ans = t - att 
    print(ans)
