# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para mais longas
VDP = int(input('Qual a distância da viagem?'))
if VDP <= 200 :
    print('O valor que você irá ter que pagar será', VDP*0.50, '.')
elif VDP > 200 :
    print('Você terá que pagar', VDP*0.45)