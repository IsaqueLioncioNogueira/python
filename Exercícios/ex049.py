# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, dessa vez use FOR.
n1 = int(input('Digite o número que deseja ver na tabuada de x1 até x10: '))
n4 = 1
n2 = 0
n3 = 1
for c in range(10):
    n4 += n3
    n2 += n1
    print(n1,'x',n4 - 1,'=',n2)