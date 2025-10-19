n = 0
total = {}

s = float(input('Digite seu salário bruto (0 para sair): '))

while s!=0:
    if s<800:
        print('Sem desconto para você')

    elif 800<=s<=1600:
        s-=(s*13/100)
        print(f'Seu novo salário é {s}')

    elif s>1600:
        s-=(s*22/100)

    horas = int(input('Quantas horas você tem trabalhado? '))

    if horas>160:
        horasn = s/160
        horasadd = horas-160
        beneficio = ((horasn/2) + horasn) * horasadd
        s += beneficio

        print(f'O seu novo salário é de {s:.2f}')

    s = round(s, 2)
    total[n] = s
    print(f'Seu salário é de {s}')
    n+=1
    s = float(input('Digite seu salário bruto: '))

print(f'O número total de salários é {total}')
print(f'O total geral é {sum(total.values()):.2f}')