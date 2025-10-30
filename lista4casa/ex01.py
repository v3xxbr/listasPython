rac = []

for i in range(9):
    rac.append(int(input('Digite o RAV: ')))

a,b,c,d,e,f,g,h,i = rac

rac[2]=h
rac[3] = g
rac[6]=c
rac[7]=d

print(f'O RAC é {rac}')