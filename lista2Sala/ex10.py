p = int(input('Digite o número de um mês (0 para sair): '))

while(p>0 and p<13):
    if p==1: print('Janeiro')
    elif p==2: print('Fevereiro')
    elif p==3: print('Março')
    elif p==4: print('Abril')
    elif p==5: print('Maio')
    elif p==6: print('Junho')
    elif p==7: print('Julho')
    elif p==8: print('Agosto')
    elif p==9: print('Setembro')
    elif p==10: print('Outubro')
    elif p==11: print('Novembro')
    elif p==12: print('Dezembro')
    p = int(input('Digite um novo mês (0 para sair): '))


print('Obrigado por participar!')
