soma = 0
maisvelho = ''
idadevelho = 0
mulheres_menos_20 = 0

for p in range(1, 5):
    print(f'----- Pessoa 0{p} -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper()
    soma += idade
    if sexo == 'M' and p == 1:
        maisvelho = nome
        idadevelho = idade
    if sexo == 'M' and idade > idadevelho:
        maisvelho = nome
        idadevelho = idade
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

mediat = soma / 4

print(f'A media de idade do grupo é: {mediat}')
print(f'O homem mais velho se chama {maisvelho} e possui {idadevelho} anos')
print(f'Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos')
    