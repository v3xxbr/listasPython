a = [] 
b = [] 
c = []

for i in range(10):
    if i<5:
        e = int(input('Digite um valor para o primeiro vetor: '))
        a.append(e)
    else:
        e = int(input('Digite um valor para o segundo vetor: '))
        b.append(e)

for u in range(5):
    c.append(a[u]-b[u])

print(f'C = {c}')