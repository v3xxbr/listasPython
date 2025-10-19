a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
div = [a, b, c]

for y in range(3):
    if div[y]%6 == 0:
        print(f'{div[y]} é divisível por 2 e por 3')
