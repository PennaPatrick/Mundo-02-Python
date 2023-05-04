peso = float(input('Digite aqui seu peso: '))
altura = float(input('Digite aqui sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')