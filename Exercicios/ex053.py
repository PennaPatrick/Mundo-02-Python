frase = str(input('Verificador de palíndromo: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

#inverso = ''                                           OPÇÃO COM LAÇO

#for letra in range(len(junto)  -1, -1 , -1):           OPÇÃO COM LAÇO
    #inverso += (junto[letra])'''

print(inverso, junto)
if inverso == junto:
    print('É um palíndromo')
else:
    print('NÃO temos um palíndromo')
    

