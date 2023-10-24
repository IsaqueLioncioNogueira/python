# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = int(input( 'Digite o ângulo usando apenas dígitos'))
seno = sin(radians(angulo))
print('O ângulo de',angulo,'tem o SENO de',seno)
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de',angulo,'tem o COSSENO de:',cosseno)
print('O ângulo de',angulo,'tem o TANGENTE de:',tangente)