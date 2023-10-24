# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dos que forem pares.
# Se for ímpar, desconsidere.
n2 = 0
for c in range(6):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0 :
        n2 += n1
print(n2)