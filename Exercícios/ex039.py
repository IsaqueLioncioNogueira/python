# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
num1 = int(input('Informe a sua idade   '))
if num1 < 18 :
    print('Você ainda vai se alistar ao serviço militar!')
elif num1 == 18 :
    print('Você já está na hora de se alistar!')
elif num1 > 18 :
    print('Você já passou da hora de se alistar!')
if num1 < 18 :
    print ( 'E falta',18 - num1 ,'anos para você se alistar!')
if num1 > 18 :
    print('Que no caso, já faz',num1 - 18,'anos que passou!')