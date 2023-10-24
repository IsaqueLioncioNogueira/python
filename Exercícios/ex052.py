# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n1 = int(input('Digite um número inteiro: '))
if n1 % 1 ==0 and n1 % 2 ==1 and n1 >= 1 :
    print('Esse número é um número primo!')
else :
    print('Esse número não é primo!')