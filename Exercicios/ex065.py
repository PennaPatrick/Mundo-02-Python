continuar = 'S'
contador = 0
media = 0
soma = 0
maior = 0
menor = 0

while continuar == 'S':
    num = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N] ').upper()
    soma += num
    contador += 1
    if contador == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / contador
print(f'Foram digitados {contador} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')

