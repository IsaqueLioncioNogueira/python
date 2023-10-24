# Faça um programa que calcule a soma entre todos os números ímpares múltiplos de 3 entre 1 e 500.
print('SOMANDO TODOS OS NÚMEROS ÍMPARES MÚLTIPLOS DE 3')
n2 = 0
for n1 in range(1,500) :
    if n1 % 2 == 1 and n1 % 3 == 0 :
        n2 += n1
print(n2)