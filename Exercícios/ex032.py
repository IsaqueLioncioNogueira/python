# Faça um programa que leia um ano qualquer e mostre se ele é bisexto.
ANO = int(input('Digite um ano em dígitos: '))
DIVISÍVELPOR4 = ANO % 4
DIVISÍVELPOR100 = ANO % 100
DIVISÍVELPOR400 = ANO % 400
if DIVISÍVELPOR4 == 0 and DIVISÍVELPOR100 != 0 or DIVISÍVELPOR400 == 0 :
    print('Esse ano é bissexto!')
else :
    print('Esse ano não é bissexto!')