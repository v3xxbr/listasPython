a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
div = [a, b]

for h in range(2):
    if div[h]%5==0 or div[h]%4==0:
        print(f'{div[h]} é divisível por 5 ou por 4')
