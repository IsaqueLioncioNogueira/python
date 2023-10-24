# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
Salario = int(input('Fale o seu salário: '))
Salario2 = Salario / 100

if Salario > 1250 :
    print('O seu salário com 10% de aumento é igual a:',Salario2 * 110,'!')
if Salario <= 1250 :
    print('O seu salário com 15% de aumento é igual a:',Salario2 * 115,'!')