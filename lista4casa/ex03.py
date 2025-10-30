RA = []

for k in range(9):
    RA.append(int(input('Digite um RA: ')))

a, b, c, d, e, f, g, h, i = RA

RA[0] = b
RA[1] = a
RA[6]=i
RA[7]=h

print(f'novoRA = {RA}')