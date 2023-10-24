# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os dez primeiros termos da progressão
# usando a estrutura while
razão = int(input('Digite a razão: '))
termo = int(input('Agora, digite o termo: '))
n1 = 0
print(termo)
while n1 != 9:
    termo += razão
    print(termo)
    n1 += 1