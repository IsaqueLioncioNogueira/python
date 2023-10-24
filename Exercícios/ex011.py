# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
a = int(input('coloque a altura: '))
l = int(input('agora,coloque a largura: '))
r = a * l
print('a quantidide de tinta para pintar a parede é: ',r/2 ,'litros de tinta')