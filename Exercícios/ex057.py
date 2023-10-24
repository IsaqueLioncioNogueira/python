# Faça um programa que leia o sexo de uma pessoa, mas só aceite os falores "M" ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Digite o sexo de uma pessoa, pode apenas ser "M" para masculino ou "F" para feminino: ')
while sexo != 'M' and sexo != 'm' and sexo != 'F' and sexo != 'f':
    sexo = input('Digite o sexo de uma pessoa, pode apenas ser "M" para masculino ou "F" para feminino: ')
print('Feito por Isaque.')