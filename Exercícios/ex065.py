# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e menor valores digitados. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.
n1 = str
n3 = 0
n4 = 0
n2 = 0
maior = n2
menor = n2
while n1 != 'N' and n1 != 'n':
    n2 = int(input('Digite um número interiro: '))
    while n2 < 0 :
        n2 = int(input('Digite um número INTEIRO: '))
        print('Números negativos NÃO são inteiros!')
    n3 += 1
    n4 += n2
    n1 = str(input('Quer continuar? (S/N): '))
    if n3 == 1:
        n2 = maior = menor
    else :
        if maior < n2:
            maior = n2
        if menor > n2:
            menor = n2
print('A média desses números foi de:',n4/n3)
print('O menor número foi o:',menor,'e o maior foi o:',maior,'.')