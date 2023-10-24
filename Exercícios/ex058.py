# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.
import random
from time import sleep
n6 = 1
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n10 = 6
n7 = 7
n8 = 8
n9 = 9
n11 = 10
conjunto = (n1,n2,n3,n4,n5,n10,n11,n9,n7,n8)
EPC = random.choice(conjunto)
print(EPC)
NEPP = int(input('Agora,tente adivinhar qual número o computador escolheu de 1 até 5 usando apenas dígitos: '))
while NEPP != EPC and NEPP != ' ':
    print('Você errou!')
    sleep(1)
    NEPP = int(input('Agora,tente adivinhar qual número o computador escolheu de 1 até 5 usando apenas dígitos: '))
    if NEPP > EPC or NEPP < EPC :
        n6 += 1
if n6 > 1 :
    print('Você precisou de',n6+1,'tentativas!')
elif n6 == 1 :
    print('Você precisou de',n6,'tentativa!')