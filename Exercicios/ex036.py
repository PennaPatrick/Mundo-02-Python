print('=' * 45)
print('V a l i d a ç ã o  D e  E m p r é s t i m o')
print('=' * 45)

valorcasa = int(input('Digite aqui o valor da casa que deseja: '))
salario = int(input('Digite aqui o seu salário: '))
tempoparcela = int(input('Em quantos anos vai pagar: '))

prestacao = valorcasa / (tempoparcela * 12)
if prestacao > 30 / 100 * salario:
    print('Empréstimo negado, Tente aumentar a quantidade de anos') 
else:
    print(f'Sua prestação ficará em R${(prestacao):.2f} mensais.')
