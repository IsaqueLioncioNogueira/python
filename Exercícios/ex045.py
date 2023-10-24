# Crie um programa que faça o computador jogar Jokempô com você.
# imports
import _operator
import builtins
import random
from _tracemalloc import stop
from msilib import sequence
from operator import contains
from timeit import repeat

# informando
y = input ( 'qual você vai escolher entre: pedra,papel e tesoura?  ' )
while y not in['pedra','papel','tesoura']:
    y = input ( 'qual você vai escolher entre: pedra,papel e tesoura?  ' )
print ( 'pedra' )
print ( 'papel' )
print ( 'tesoura!' )

# escolhendo
j = ['pedra', 'papel', 'tesoura']
_operator
def contains(pedra, papel, tesoura) : var = contains in y
resultado = random.choice ( j )
print ( ' ' )
print ( ' ' )
print ( '{}'.format ( resultado ) )
#1
if resultado == ['pedra'] and y == ['tesoura'] :
    print('Eu ganhei!')
elif resultado == ['pedra'] and y == ['pedra'] :
    print('Deu empate, reinicie o programa e tente denovo!')
elif resultado == ['pedra'] and y == ['papel'] :
    print('Você ganhou!')
#2
elif resultado == ['papel'] and y == ['pedra'] :
    print('Eu ganhei!')
elif resultado == ['papel'] and y == ['papel'] :
    print('Deu empate, reinicie o programa e tente denovo!')
elif resultado == ['pedra'] and y == ['tesoura'] :
    print('Você ganhou!')
#3
elif resultado == ['tesoura'] and y == ['papel'] :
    print('Eu ganhei!')
elif resultado == ['tesoura'] and y == ['tesoura'] :
    print('Deu empate, reinicie o programa e tente denovo!')
elif resultado == ['tesoura'] and y == ['pedra'] :
    print('Você ganhou!')
