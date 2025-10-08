p1 = float(input('Digite a nota da 1a avaliação: '))
p2 = float(input('Digite a nota da 2a avaliação: '))
ativ = float(input('Digite a nota das atividades: '))

media = (p1*4 + p2*4 + ativ*2)/10

print(f'A sua média semestral é de {media:.2f}.')