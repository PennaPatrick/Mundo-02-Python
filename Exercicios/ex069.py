idade = 0
contador = 0
homens = 0
mulheresmenos20 = 0

while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA  ')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = (input('Sexo: [M/F] ')).upper()

    if idade > 18:
        contador += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    print('-' * 25)
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        print('=== Cadastros Realizados ===')
        print(f'Total de pessoas com mais de 18 anos: {contador}')
        print(f'Ao todo temos {homens} homens cadastrados')
        print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos')
        break
