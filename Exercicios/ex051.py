num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = num + (10-1) * razao

for c in range(num, decimo+razao, razao):
    print(f'{c}', end=' -> ')
print('Acabou')
