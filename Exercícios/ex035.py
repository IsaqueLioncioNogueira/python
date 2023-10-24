# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo.
num1 = float(input('Digite o tamanho da primeira reta: '))
num2 = float(input('Digite o tamanho da segunda reta: '))
num3 = float(input('Digite o tamanho da terceira reta: '))
num4 = num1 / 3
if num1 == num2 and num1 == num3 :
    print('Dá para você formar um triângulo!')
else :
    print('Você não consegue formar um triânuglo!')