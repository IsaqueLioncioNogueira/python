# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
Massa = float(input('Digite seu peso: '))
Tamanho = float(input('Agora, digite seu tamanho: '))
IMC = Massa / Tamanho
if IMC < 18.5 :
    print('Você está abaixo do peso')
elif 18.5 <= IMC < 25 :
    print('Você está com o peso ideal! ')
elif 25 <= IMC < 30 :
    print('Você passou do peso ideal :(')
elif 30 >= IMC < 40 :
    print('Ixe, aqui pelos meus cálculos você está obeso!')
elif IMC > 40 :
    print('Você está com obesidade mórbida!')