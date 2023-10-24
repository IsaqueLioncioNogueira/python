# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou o empréstimo será negado.
num1 = int(input('O valor da casa: '))
num2 = int(input('O seu salário: '))
num3 = int(input('Em quantos anos você irá pagar: '))
num4 = num3 * 12
num5 = num2 / 100
if num1 <= (30 * num5) :
    print('Nós iremos te emprestar o dinheiro!')
else :
    print('Nós não podemos te emprestar o dinheiro pois a prestação mensal tem que ser abaixo de 30% de seu salário!')