from random import randint
print('-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-' * 30)

bot = soma = contador = 0

while True:
    bot = randint(1,10)
    num = int(input('Digite um número: '))
    op = input('Par ou Ímpar [P/I] ').upper()
    print('=' * 30)
    soma = bot + num
    if op == 'P':
        if soma % 2 == 0:
            print('Você ganhou! Continue...')
            contador += 1
        else:
            print(f'Você perdeu! Sua WinStreak foi de {contador} vitórias')
            break
    if op == 'I':
        if soma % 2 == 0:
            print(f'Você perdeu! Sua WinStreak foi de {contador} vitórias')
            break
        else:
             print('Você ganhou! Continue...')
             contador += 1