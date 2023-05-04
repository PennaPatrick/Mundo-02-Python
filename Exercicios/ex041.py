from datetime import date
nasc = int(input('Digite aqui o ano de nascimento do atleta: '))
confirmacao = date.today().year - nasc

if confirmacao <= 9:
    print('MIRIM')
elif confirmacao <= 14 and confirmacao > 9:
    print('INFANTIL')
elif confirmacao <= 19 and confirmacao > 14:
    print('JUNIOR')
elif confirmacao <= 20 and confirmacao > 19:
    print('SÊNIOR')
else:
    print('MASTER')
