# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final.
# de acordo com a média atingida.
# Média abaixo de 5, reprovado
# Média entre 5 e 6.9, recuperação
# Média 7 ou superior, aprovado.
num1 = float(input('Digite a sua nota: '))
num2 = float(input('Digite a sua segunda nota:  '))
num3 = (num1 + num2) / 2
print('A média é:',num3,'.E por isso, vou ter que calcular para ver se você passou de ano ou não')
if num3 < 5:
    print('Ehhh, pelos meus cálculos, você ficou reprovado!')
elif num3 >= 5 and num3 < 7 :
    print('Ixe, tu ficou de recuperação!')
elif num3 >= 7 :
    print('Uau! Você passou!')