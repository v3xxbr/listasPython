media=0
for i in range(4):
    n = float(input(f'Digite a nota do {i+1} bimestre: '))
    media+=n

media=(media/4)

print(f'A média anual é de {media:.2f}.')