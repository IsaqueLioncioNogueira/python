# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua
# categoria, conforme a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master
print('                 CONFEDERAÇÃO FISCAL DE NATAÇÃO')
N1 = int(input('Digite sua idade: '))
if N1 <= 9 :
    print('A sua classificação é: Mirim')
elif 14 >= N1 >= 10 :
    print('A sua classificação é: Infantil')
elif 19 >= N1 >= 15 :
    print('A sua classificação é: Júnior')
elif 20 >= N1 > 19 :
    print('A sua classificação é: Sênior')
elif N1 > 20 :
    print('A sua classificação é: Master')