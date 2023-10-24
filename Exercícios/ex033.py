# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
Num1 = float(input('Fale o primeiro número: '))
Num2 = float(input('Fale o segundo número: '))
Num3 = float(input('Fale o terceiro número: '))
if Num1 > Num2 and Num3 < Num1 :
    print('O ',Num1,'é o maior')
elif Num2 > Num1 and Num3 < Num2 :
    print('O ',Num2,'é o maior')
elif Num3 > Num1 and Num2 < Num3 :
    print('O ',Num3,'é o maior')
if Num1 < Num2 and Num3 > Num1 :
    print('E o ',Num1,'é o menor')
elif Num2 < Num1 and Num3 > Num2 :
    print('E o ',Num2,'é o menor')
elif Num3 < Num1 and Num2 > Num3 :
    print('E o ',Num3,'é o menor')