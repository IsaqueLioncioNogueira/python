# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
n1 = str
n2 = 0
n3 = 0
n4 = str
n5 = 0
m = 0
vez = 0
nm = 0
while n4 != 'N' and n4 != 'n':
    n1 = input('Digite o nome de um produto: ')
    vez += 1
    n2 = float(input('Agora, digite o valor: '))
    while n2 < 0:
        n2 = int(input('Digite o valor: '))
    n4 = input('Quer continuar? [S/N] ')
    while n4 != "s" and n4 != "S" and n4 != "n" and n4 != "N":
        n4 = input('Quer continuar? [S/N] ')
    n3 += n2
    if n2 > 1000:
        n5 += 1
    if vez == 1:
        m = n2
    elif vez >= 2 and n2 < m:
        nm = n1
if n5 == 1:
    print('O total gasto foi de: R$', n3, 'tem  1  produto que custa mais de R$1000,00 e o nome do produto mais barato é:', nm)
else:
    print('O total gasto foi de: R$', n3, 'tem', n5, 'produtos que custa mais de R$1000,00 e o nome do produto mais barato é:', nm)