# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# Calcule e mostre o comprimento da hipotenusa.

#Diálogo
print('Décima sétima aula do professor Isaque...Vamos lá!')
print('Professor,o que vamos fazer hoje??')
print('Ahh! Hoje nós iremos aprender sobre cateto oposto,cateto adjacente e como calcular o comprimento da hipotenusa!')
print('Ok então professor Isaque!')
print('Mas você pode me chamar apenas de Isaque?')
print('Posso sim!')
print('Então sem delongas, vamos para a aula!')

#Código
co = int(input('Vamos ter que informar primeiro o comprimento do cateto oposto! Para informar sempre lembre de usar apenas dígitos! '))
ca = int(input('Agora, vamos ter que informar por segundo o comprimento do cateto adjacente! '))
hi = (co**2+ca**2) ** (1/2)
print('Crianças, pelos meus cálculos, o comprimento da hipotenusa é igual a: ',hi)

#Diálogo (de novo)
print('Lembrando que para conseguir o resultado do comprimento da hipotenusa sempre é preciso de exponencializar os dois catetos e depois, com os dois resultados, você deve somar um com o outro e, assim você terá: ')
print('O valor da hipotenusa!')