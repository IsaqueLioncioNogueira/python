# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
n1 = int(input('Coloque a velicidade de seu carro em dígitos: '))
n2 = n1 - 80
if n2 == 0 :
    print('Você não irá ter que pagar multa!')
elif n2 > 0:
    print('Você irá ter que pagar uma multa de:',n2 * 7,'reais!')