# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
razão = int(input('Digite a razão: '))
termo = int(input('Agora, digite o termo: '))
print(termo)
for c in range(9):
    termo += razão
    print(termo)