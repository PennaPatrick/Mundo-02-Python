print('=' * 25)
print('   LOJA SUPER BARATAO')
print('=' * 25)

soma = maisque1000 = 0
continuar = ''
barato = ''
baratop = 0
cont = 0

while True:
    nome = input('Nome do Produto: ')
    preço = int(input('Preço: R$'))
    cont += 1
    if cont == 1 or preço < baratop:
        baratop = preço
        barato = nome
    soma += preço
    if preço > 1000:
        maisque1000 += 1
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break

print(f'O total da compra foi: R${(soma):.2f}')
print(f'Temos {maisque1000} produtos que custam mais que R$1000,00')
print(f'O produto mais barato foi {barato} que custou R${(baratop):.2f}')

