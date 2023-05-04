a = int(input('Digite aqui o primeiro comp: '))
b = int(input('Digite aqui o segundo comp: '))
c = int(input('Digite aqui o terceiro comp: '))

if a + b > c and b + c > a and c + a > b:
    print('Podemos formar um triangulo')
    if a == b and b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')

else:
    print('Não é possivel formar um triangulo')

    