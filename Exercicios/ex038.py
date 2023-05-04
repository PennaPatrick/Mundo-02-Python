num1 = int(input('Escreva aqui o primeiro número: '))
num2 = int(input('Escreva aqui o segundo número: '))

if num1 > num2:
    print(f'{num1} é o maior valor')
    print(f'{num2} é o menor valor')
elif num2 > num1:
    print(f'{num2} é o maior valor')
    print(f'{num1} é o menor valor')
else:
    print('Não existe valor maior, os dois são iguais')