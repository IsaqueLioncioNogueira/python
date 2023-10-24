# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o utilizador digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a ‘flag’).
n1 = int(input('Digite um número(Digite 999 para encerrar o programa): '))
n2 = 0
n3 = 0
n2 += 1
n3 += n1
FlagAtivada = True
while FlagAtivada and n1 != 999:
    resultado = n1 = int(input('Digite um número(Digite 999 para encerrar o programa): '))
    n2 += 1
    n3 += n1
    if n1 == 999:
        FlagAtivada = False
if n1 == 999 :
    print('Você digitou',n2-1,'números e a soma entre eles deu:',n3-999)