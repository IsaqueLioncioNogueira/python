# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

print('|-----------------------------------------|')
print('|                                         |')
print('|                                         |')
print('|                                         |')
print('|                                         |')
print('|        CONCESSECIONÁRIA                 |')
print('|               DO                        |')
print('|             ISAQUE                      |')
print('|                                         |')
print('|                                         |')
print('|                                         |')
print('|                                         |')
print('|                                         |')
print('|_________________________________________|')


apd = int(input('Coloque um número que equivale ao tempo em dias de seu aluguel com o carro usando apenas dígitos: '))
km=int(input('Agora, coloque o número que se equivale aos quilômetros rodados no carro alugado usando apenas dígitos: '))
t = apd*60
t2 = km/100
t3 = t2*15
print('você terá que pagar ',t+t3)