num = int(input('Primeiro Termo: '))
termo = num
razao = int(input('Razão da PA: '))
contador = 0

while contador < 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    contador += 1
print('FIM')
