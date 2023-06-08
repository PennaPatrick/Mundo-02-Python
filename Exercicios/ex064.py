num = 0
contador = 0
soma = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    contador += 1

print(f'Você digitou {contador - 1} números e a soma entre eles foi {soma - 999}')
