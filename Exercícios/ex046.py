# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício.
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep



print('CONTAGEM REGRESSIVA DOS FOGOS')
time = 10
while time > 0:
    print(time)
    sleep(1)
    time -= 1
print('OS FOGOS FORAM SOLTOS!!!')
