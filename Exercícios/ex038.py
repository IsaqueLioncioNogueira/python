# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
num1 = int(input('Digite o primeiro valor:  '))
num2 = int(input('Digite o segundo valor:  '))
if num2 > num1 :
    print('O',num2,'é maior que o',num1,'.')
elif num2 < num1 :
    print('O',num1,'é maior que o',num2,'.')
elif num2 == num1 :
    print('Nenhum dois dois valores é maior')