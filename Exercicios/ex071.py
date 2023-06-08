print('=' * 30)
print('        BANCO CINZINHA')
print('=' * 30)

saque = int(input('Digite o valor desejado para saque: R$'))
cel50 = cel20 = cel10 = cel1 = 0
while True:
    if (saque / 50) >= 1:
        cel50 = saque // 50
        saque = saque % 50
    if (saque / 20) >= 1:
        cel20 = saque // 20
        saque = saque % 20
    if (saque / 10) >= 1:
        cel10 = saque // 10
        saque = saque % 10
    if (saque / 1) >= 1:
        cel1 = saque
    break
print(f'Total de {cel50} células de R$50')
print(f'Total de {cel20} células de R$20')
print(f'Total de {cel10} células de R$10')
print(f'Total de {cel1} células de R$1')


