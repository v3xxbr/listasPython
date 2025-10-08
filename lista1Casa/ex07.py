import math

r = float(input('Digite o raio da esfera (cm): '))
v = (4/3)*math.pi*(r**3)
area = 4*math.pi*(r**2)

print(f'A área da superfície desta esfera é {area:.2f}cm^2.\nO Volume desta esfera é de {v:.2f}cm^3.')