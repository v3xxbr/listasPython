a = []
b = []
c = []

for m in range(10):
    if m<5:
        a.append(int(input(f'Digite o {m+1}o valor da primeira matriz: ')))
    else:
        b.append(int(input(f'Digite o {(m-5)+1}o valor da segunda matriz: ')))

c = a + b

print(f'C = {c}')
