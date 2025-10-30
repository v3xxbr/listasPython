a = []
b = []

for t in range(6):
    h = int(input(f'Digite o {t+1}o valor da matriz: '))
    a.append(h)

def fatorial(n):
    fat=1
    for i in range(n, 0, -1):
        fat *= i

    return fat

for k in a:
    b.append(fatorial(k))

print(f'B = {b}')