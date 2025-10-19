c = int(input('Digite seu código de curso (0 para sair): '))

while c>0 and c<6:
    if c==1: print('Engenharia')
    elif c==2: print('Edificações')
    elif c==3: print('Sistemas Elétricos')
    elif c==4: print('Turismo')
    elif c==5: print('Análise de Sistemas')

    c = int(input('Digite um novo código (0 para sair): '))

print('Obrigado por participar!')