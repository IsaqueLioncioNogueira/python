# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo.
# Desconsiderando os espaços.
frase = input('Digite uma frase: ')
frase2 = frase.replace(' ','')
frase3 = frase2.lower()
frase4 = frase3[::-1]
if frase3 == frase4 :
    print('Essa frase é um palíndromo!')
else :
    print('Essa frase não é um palíndromo!')