# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo utilizador.
# O programa será interrompido quando o número solicitado for negativo.
n1 = 0
n2 = 0
while n1 >= 0 :
    n1 = int(input('Digite um número para visualisar a tabuada dele: '))
    while n2 != 10 and n1 >= 0:
        n2 += 1
        print(n1, 'x', n2, '=', n1*n2)
    n2 -= 10
    if n1 < 0 :
        print('----------------------PROGRAMA INTERROMPIDO----------------------')