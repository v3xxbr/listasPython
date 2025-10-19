media=0

for i in range(3):
    n = float(input(f'Digite o valor da {i+1} nota: '))

    while n>10 or n<0:
        n = float(input(f'Digite o valor da {i+1} nota: '))
    media += n

media /= 3

print(f'Sua média é {media:.2f}')

if(media>=6):
    print('Aprovado!')
else:
    print('Reprovado!')
