import math

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

delta = (b**2) - 4*(a)*(c)

if delta<0:
   print('Essa equação não possui números reais.')

else:
    x1=(b*-1-(math.sqrt(delta)))/2*(a)
    x2=(b*-1+(math.sqrt(delta)))/2*(a)
    print(f'As raízes são {x1:.2f} e {x2:.2f}')