# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa
# O programa deverá realizar a operação selecionada em cada caso.
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Agora, digite 1 para somar esses dois números,2 para multiplicar,3 para saber qual é o maior,4 para digitar novos números,e 5 para sair do programa.'))
while n3 != 5 :
    if n3 == 1:
        print('A soma desses dois números tem o total de:',n1+n2)
        n3 = int(input('Agora, digite 1 para somar esses dois números,2 para multiplicar,3 para saber qual é o maior,4 para digitar novos números,e 5 para sair do programa.'))
    if n3 == 2:
        print('A multiplicação do número',n1,'pelo número',n2,'é igual a:',n1*n2)
        n3 = int(input('Agora, digite 1 para somar esses dois números,2 para multiplicar,3 para saber qual é o maior,4 para digitar novos números,e 5 para sair do programa.'))
    if n1 > n2 and n3 == 3:
        print('O maior número é o:', n1)
        n3 = int(input('Agora, digite 1 para somar esses dois números,2 para multiplicar,3 para saber qual é o maior,4 para digitar novos números,e 5 para sair do programa.'))
    elif n2 > n1 and n3 == 3:
        print('O maior número é o:', n2)
        n3 = int(input('Agora, digite 1 para somar esses dois números,2 para multiplicar,3 para saber qual é o maior,4 para digitar novos números,e 5 para sair do programa.'))
    elif n2 == n1 and n3 == 3:
        print('Nenhum dos dois é o maior!')
        n3 = int(input('Agora, digite 1 para somar esses dois números,2 para multiplicar,3 para saber qual é o maior,4 para digitar novos números,e 5 para sair do programa.'))
    if n3 == 4 :
        print('Reiniciando...')
        sleep(1)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        n3 = int(input('Agora, digite 1 para somar esses dois números,2 para multiplicar,3 para saber qual é o maior,4 para digitar novos números,e 5 para sair do programa.'))

if n3 == 5:
    print('-------------------------FIM DO PROGRAMA-------------------------')