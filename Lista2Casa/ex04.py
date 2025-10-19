a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

k = (a,b,c)

print(f'O maior número é {max(k)}')
print(f'O menor número é {min(k)}')

k = sorted(k)

print(f'O número do meio é {k[1]}')