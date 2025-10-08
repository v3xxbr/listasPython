import math
raio = float(input('Digite o raio da circunferência (cm): '))

area = math.pi*(raio**2)
comp = 2*math.pi*raio

print(f'A área desta circuferência é de {area:.2f}cm^2,\n já seu comprimento é de {comp:.2f}cm.')