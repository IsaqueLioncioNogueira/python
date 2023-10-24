# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
a = input('digite algo: ')
print('o tipo primitivo desse valor é', type(a))
print('apenas espaços?', a.isspace())
print('apenas numeros?', a.isnumeric())
print('apenas letras?', a.isalpha())
print('tem letras e numeros?', a.isalnum())
print('tem apenas letras maiusculas?', a.isupper())
print('tem apenas letras minusculas?', a.islower())
print('está capitalizada?', a.istitle())