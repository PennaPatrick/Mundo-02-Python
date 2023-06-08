p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = int(input('Número de termos: '))
c = 0

while c < d + 1:
    print(f'{p}', end='➡ ')
    p += r
    c += 1
    if c == d:
        print('ACABOU!\n')
    if c == d:
        d = int(input('Você quer adicionar mais alguns termos? Quantos? '))
        if d > 0:
            c = 0
        elif d == 0:
            c += 1