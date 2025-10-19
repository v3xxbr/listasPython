a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a<b+c and b<a+c and c<a+b:
    if a==b and b==c:
        print('Equilátero.')
    elif a==b or b==c or c==a:
        print('Isóceles.')
    elif a!=b and a!=c and b!=c:
        print('Escaleno.')
else:
    print('Não é um triângulo.')
