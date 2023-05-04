preço = float(input('Valor do produto: R$'))
pagamento = int(input('''Qual forma de pagamento?
        [1] Dinheiro/Cheque
        [2] Cartão Avista
        [3] 2x Cartão
        [4] 3x ou mais Cartão         '''))


if pagamento == 1:
    valor = preço * 0.9
    print(f'Ficara no total de R${valor}')
elif pagamento == 2:
    valor = preço * 0.95
    print(f'Ficara no total de R${valor}')
elif pagamento == 3:
    valor = preço
    parcela = valor / 2
    print(f'Ficara no total de R${valor} com 2 parcelas de R${(parcela):.2f}')
elif pagamento == 4:
    x = int(input('Quantidade de parcelas: '))
    valor = preço * 1.2
    parcela = valor / x
    print(f'Ficara no total de R${valor} com {x} parcelas de R${(parcela):.2f}')
else:
    print('Escolha uma forma valida de pagamento dentre as alternativas')
