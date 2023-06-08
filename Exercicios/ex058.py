import random

num = random.randint(0, 11)
escolha = int(input('Escolha um número: '))
tentativas = 0

while escolha != num:
    escolha = int(input('Haha, você errou. Tente novamente: '))
    tentativas += 1
print(f'Parabéns vc acertou o número! mas precisou de {tentativas} tentativas')
