r = input('Digite a operação desejada (S para sair): ')
r = (r.strip()).lower()
num = []

while r!='s':
    for g in range(0,2):
        p = float(input(f'Digite o {g+1}o número: '))
        num.append(p)

    if r=='+': print(f'{num[0]} + {num[1]} = {num[0] + num[1]}')
    elif r=='-': print(f'{num[0]} - {num[1]} = {num[0] - num[1]}')
    elif r=='': print(f'{num[0]} {num[1]} = {num[0] * num[1]}')
    elif r=='/': print(f'{num[0]} / {num[1]} = {num[0] / num[1]}')

    num.clear()
    r = input('Digite a operação desejada (S para sair): ')
    r = (r.strip()).lower()

print('Obrigado por participar!') 
