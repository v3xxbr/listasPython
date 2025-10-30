a = []
b = []

for n in range(10):
    a.append(int(input(f'Digite o {n+1} valor: ')))
    b.append(a[-1])

b = sorted(b, reverse=True)

print(f'B = {b}')