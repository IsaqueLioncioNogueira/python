# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
n1 = str
n2 = 0
n5 = 0
n6 = 0
while n1 != 'n' and n1 != 'N':
    n3 = int(input('Digite o sexo de uma pessoa, 1 para homem e 2 para mulher: '))
    while n3 != 1 and n3 != 2 :
        n3 = int(input('Digite o sexo de uma pessoa, 1 para homem e 2 para mulher: '))
    n4 = int(input('Digite a idade dessa pessoa: '))
    n1 = input('Quer continuar? ')
    while n1 != 'S' and n1 != 's' and n1 != 'n' and n1 != 'N':
        n1 = input('Quer continuar? ')
    if n4 > 18:
        n2 += 1
    if n3 == 1:
        n5 += 1
    elif n3 == 2 and n4 <= 20:
        n6 += 1
print('Tem',n2,'pessoas com mais de 18 anos,foram cadastrados',n5,'homens e tem ',n6,'mulheres com menos de 20 anos.')