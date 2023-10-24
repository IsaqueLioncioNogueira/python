# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999.
# Que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# Desconsidere o 999
n1 = 0
n2 = 0
n3 = 0
while n1 != 999:
    n1 = int(input('Para parar o programa você tem que digitar o número 999.Digite um número: '))
    if n1 != 999:
        n2 += n1
        n3 += 1
print('Foram digitados',n3,'números sem contar o 999,e a soma desses números sem contar o 999 é',n2)