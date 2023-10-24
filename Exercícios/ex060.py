# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120
n1 = int(input('Digite um número: '))
n2 = n1
print(n1,'!')
print(' = ')
print(n1,'x')
while n1 != 1 :
    n1 -= 1
    print(n1,'x')
    n2 *= n1
print('=')
print(n2)