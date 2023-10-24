# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário, 2 para octal e 3 para hexadecimal


n1 = int(input('Digite um número  '))
n2 = int(input('Agora, 1 para binário, 2 para octal e 3 para hexadecimal'))
n3 = bin(n1)
n4 = oct(n1)
n5 = hex(n1)
if n2 == 1 :
    print('O número',n1,'em formato de código binário é igual a:',n3)
elif n2 == 2 :
    print('O número',n1,'em formato de código binário é igual a:',n4)
elif n2 == 3 :
    print('O número',n1,'em formato de código binário é igual a:',n5)