# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
c = input('coloque o produto: ')
n = int(input('coloque um valor: '))
r = n/100
d = r * 95
print('Você irá ter 5% de desconto no(a)!',c,'. Seu novo preço é: ',d)