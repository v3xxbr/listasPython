RA = []
novoRA = []

for k in range(9):
    RA.append(int(input('Digite um RA: ')))
    novoRA.append(RA[-1])

for i in range(3):
    novoRA[5+i] = RA[8-i]

print(f'Novo RA = {novoRA}')