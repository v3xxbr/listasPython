dt = float(input('Informe o tempo gasto (h): '))
vm = float(input('Informe a velocidade média (km/h): '))

ds = vm*dt

litros = ds/12

print(f'Foram gastos {litros:.2f} litros nessa viagem.')