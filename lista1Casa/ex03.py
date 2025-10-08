ap = float(input('Informe a altura da parede: '))
lp = float(input('Informe a largura da parede: '))

aa = float(input('Informe a altura do azulejo: '))
la = float(input('Informe a largura do azulejo: '))

qtdd = (ap*lp)/(aa*la)

print(f'É (são) necessário(s) {qtdd:.1f} azulejo(s).')