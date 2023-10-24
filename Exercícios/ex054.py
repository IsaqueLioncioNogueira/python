# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere maioridade 21 anos
n2 = 0
n3 = 0
for c in range(7):
    n1 = int(input('Digite a idade de uma pessoa: '))
    if n1 < 21 :
        n3 += 1
    if n1 >= 21 :
        n2 += 1
print(n2,'pessoas já atingiram a maioridade!')
print('E',n3,'pessoas ainda não atingiram.')
print('---------------FIM---------------')