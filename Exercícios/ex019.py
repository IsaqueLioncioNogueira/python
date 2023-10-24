# O professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o sorteado.
import random
# Diálogo
print('Décima nona aula do professor Isaque,acabou...Vou ter que sortear alguém no quadro?')
print('Sim!')
print('Ok,vou pedir para o meu amigo que também é um professor para sortear!')
print('Ok então professor Isaque!')
print('Mas você pode me chamar apenas de Isaque?')
print('Posso sim!')
print('Então sem delongas, vou chamar ele!')

# Código
n1 = input('Qual o primeiro aluno?  ')
n2 = input('Qual o segundo aluno?  ')
n3 = input('Qual o terceiro aluno? ')
n4 = input('E o quarto aluno? ')
turma = (n1, n2, n3, n4)
escolhido = random.choice(turma)
print('Dentre todas essas crianças ', turma, '. Eu vou escolher o(a)',escolhido, '!')