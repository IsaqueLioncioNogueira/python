# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor.
maior = 0
menor = 0
for c in range(5):
    n1 = float(input('Digite o peso de uma pessoa: '))
    if n1 >= maior :
        maior = n1
    elif n1 < maior :
        menor = n1
print('O menor número que você digitou foi o:',menor,'e o maior foi o:',maior)