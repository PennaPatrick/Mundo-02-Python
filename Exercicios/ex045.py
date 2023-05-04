from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('=' * 20)
print(f'BOT /// {itens[bot]} Vs {itens[jogador]} ///  PLAYER ')
print('=' * 20)

if bot == 0: # PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA')
    elif jogador == 2:
        print('DERROTA')
    else:
        print('JOGADA INVÁLIDA')


elif bot == 1: # PAPEL
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITÓRIA')
    else:
        print('JOGADA INVÁLIDA')

elif bot == 2: #TESOURA
    if jogador == 0:
        print('VITÓRIA')
    elif jogador == 1:
        print('DERROTA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
