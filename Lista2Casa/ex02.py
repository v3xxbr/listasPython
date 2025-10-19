import random

m = int(input('Digite um número entre 0 e 100: '))

while m<0 or m>100:
    m = int(input('O número deve estar entre 0 e 100: '))

chave = random.randint(0, 100)

m -= chave
m = abs(m)

print(f'O valor chave é {chave}, portanto a diferença é {m}.')