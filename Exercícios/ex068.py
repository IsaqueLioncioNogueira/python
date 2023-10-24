# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
from time import sleep

n5 = 0
n4 = 0
LDC = (1,2,3,4,5,6,7,8,9,10)
while n4 != 2 :
    n1 = int(input("Digite '1' para par e '2' para ímpar: "))
    while 2 < n1 <= 0 :
        n1 = int(input("Digite '1' para par e '2' para ímpar: "))
    if n1 == 1 :
        n2 = 2
    if n1 == 2 :
        n2 = 1
    n3 = int(input('Agora, digite um número até 10: '))
    while n3 > 10 :
        n3 = int(input('Agora, digite um número até 10: '))
    NE = random.choice(LDC)
    if n2 == 1 and (NE + n3) % 2 == 0 :
        n4 = 2
    if n2 == 2 and (NE + n3) % 2 != 0 :
        n4 = 2
    if n2 == 1 and (NE + n3) % 2 != 0 :
        n4 = 1
    if n2 == 2 and (NE + n3) % 2 == 0 :
        n4 = 1
    print(NE)
    if n4 == 1 :
        n5 += 1
    if n4 == 1:
        print('Você ganhou!')
        sleep(1)
if n5 > 1 :
    print('Você fez',n5,'vitórias consecutivas!')
if n5 <= 1:
    print('Você fez',n5,'vitória consecutiva!')