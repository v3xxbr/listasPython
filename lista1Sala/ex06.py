valor = float(input('Qual o capital inicial? '))
taxa = float(input('Qual o valor da taxa? '))
tempo = float(input('Qual o tempo da prestação (mês)? '))

prestacao = valor + (valor*(taxa/100)*tempo)

print(f'O valor da prestação é de R${prestacao:.2f}.')