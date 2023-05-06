from datetime import date

atual = date.today().year
adultos = 0
midade = 0
for c in range(1, 8):
    nasc = int(input('Digite os anos de nascimento: '))
    if atual - nasc >= 21:
        adultos += 1
    else:
        midade += 1

print(f'O total de maiores de idade são: {adultos}')
print(f'O total de menores de idade são: {midade}')