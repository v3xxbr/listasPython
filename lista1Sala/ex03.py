import math

r = float(input('Informe o raio da lata (cm): '))
altura = float(input('Informe a altura da lata(cm): '))

v = math.pi * (r**2) * altura

print(f'O volume desta lata é de {v:.2f}cm^3.')