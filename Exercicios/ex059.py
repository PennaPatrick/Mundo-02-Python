num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

soma = 0
produto = 0
maior = 0

menu = int(input('''
=-=-=-=-=-=-=
[1]Somar
[2]Multiplicar    
[3]Maior
[4]Novos números
[5]Sair do Programa 
>>> Qual opção desejada: '''))

while menu < 5:
    if menu == 1:
        soma += num1 + num2
        print(f'A soma entre {num1} + {num2} é: {soma}')
    if menu == 2:
        produto += num1 * num2
        print(f'O produto de {num1} x {num2} é: {produto}')
    if menu == 3:
        if num1 > num2:
            maior += num1
        else:
            maior += num2
        print(f'O maior número é: {maior}')
    if menu == 4:
        num1 = num1 - num1
        num2 == num2 - num2
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))

    soma = 0
    produto = 0
    maior = 0
    menu = int(input('''
=-=-=-=-=-=-=
[1]Somar
[2]Multiplicar    
[3]Maior
[4]Novos números
[5]Sair do Programa 
>>> Qual opção desejada: '''))
if menu == 5:
    print('O programa foi finalizado')
    
