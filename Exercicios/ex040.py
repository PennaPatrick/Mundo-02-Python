n1 = int(input('Digite aqui a nota do primeiro semestre: '))
n2 = int(input('Digite aqui a nota do segundo semestre: '))

media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('PARABÉNS, APROVADO!')