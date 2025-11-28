n = input().strip() 
freq = [0] * 26

for i in n:
    freq[ord(i) - ord('A')] += 1

oddc = 0
odd_i = -1

for i in range(26):
    if freq[i] % 2 == 1:
        oddc += 1
        odd_i = i 

if oddc > 1:
    print('NO SOLUTION')
else:
    izq = []

    for j in range(26):
        izq.append(chr(ord('A') + j) * (freq[j] // 2))

    iz = "".join(izq)

    if odd_i != -1:
        m = chr(ord('A') + odd_i) * (freq[odd_i] % 2)
    else:
        m = ""

    der = iz[::-1]
    print(iz + m + der)

