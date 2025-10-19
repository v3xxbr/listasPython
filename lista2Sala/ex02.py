n1 = float(input('Digite a nota da primeira nota: '))
n2 = float(input('Digite a nota da segunda nota: '))

media = (n1+n2)/2

if(media>=6):
    print(f'Sua média é {media:.2f} ! Você foi aprovado!')
else:
    exame = float(input('Informe a nota do exame: '))
    media = (exame+media)/2
    if(media >=5):
        print(f'Sua média é {media:.2f} ! Você foi aprovado em exame!')
    else:
        print(f'Sua média é {media:.2f} ! Você foi reprovado!')
