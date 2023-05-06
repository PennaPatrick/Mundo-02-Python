soma = 0
soma2 = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
    elif num % 2 != 0:
        soma2 += num
print(soma)
print(soma2)
