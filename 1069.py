dna = input()

m_len = 1
suma = 1

for i in range(1, len(dna)): 
    if dna[i] == dna[i-1]: 
        suma += 1 
    else: 
        if suma > m_len: 
            m_len = suma 
        suma = 1 

if suma > m_len: 
    m_len = suma 

m_len = max(m_len, suma)
print(m_len)
