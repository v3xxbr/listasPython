dt = float(input('Informe o tempo gasto (h): '))
vm = float(input('Informe a velocidade média (km/h): '))

ds = vm*dt

litros = ds/12

print(f'Velocidade Média: {vm:.2f} km/h')
print(f'Tempo: {dt:.2f} h')
print(f'Distância: {ds:.2f} km')
print(f'Foram gastos {litros:.2f} litros nessa viagem.')