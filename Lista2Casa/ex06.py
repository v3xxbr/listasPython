m = int(input('Digite o número de um mês (0 para sair): '))

while(m>0 and m<13):
    if m==1: print('Janeiro')
    elif m==2: print('Fevereiro')
    elif m==3: print('Março')
    elif m==4: print('Abril')
    elif m==5: print('Maio')
    elif m==6: print('Junho')
    elif m==7: print('Julho')
    elif m==8: print('Agosto')
    elif m==9: print('Setembro')
    elif m==10: print('Outubro')
    elif m==11: print('Novembro')
    elif m==12: print('Dezembro')
    m = int(input('Digite um novo mês (0 para sair): '))


print('Obrigado por participar!')