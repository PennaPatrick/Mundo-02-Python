n = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 15)
    if n < 0:
        print('Programa encerrado')
        break
    for mult in range(1, 11):
        print(f'{n} x {mult} = {n * mult}')
    print('-' * 15)

