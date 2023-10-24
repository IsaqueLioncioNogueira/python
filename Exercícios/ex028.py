# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
conjunto = (n1,n2,n3,n4,n5)
EPC = random.choice(conjunto)
print(EPC)
NEPP = int(input('Agora,tente adivinhar qual número o computador escolheu de 1 até 5 usando apenas dígitos: '))
if NEPP > EPC:
    print('Você errou!')
elif NEPP < EPC:
    print('Você errou!')
else :
    print('Você acertou!')