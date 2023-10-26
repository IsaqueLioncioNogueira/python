# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
valor = float(input('Digite um valor a ser sacado: '))
while valor < 1:
    n1 = float(input('Digite um valor a ser sacado: '))
while valor != 0:
    if valor >= 50:
        valor -= 50
        nota1 += 1
    if valor >= 20:
        valor -= 20
        nota2 += 1
    if valor >= 10:
        valor -= 10
        nota3 += 1
    if valor >= 1:
        valor -= 1
        nota4 += 1
print('Serão entregues',nota1,'nota(s) de R$50,00,',nota2,'nota(s) de R$20,00,',nota3,'nota(s) de R$10,00,',nota4,'nota(s) de R$1,00.')