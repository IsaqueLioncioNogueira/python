# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#Diálogo
from random import shuffle
import random
print('Hoje eu estou um pouco cansado de sempre ter que pedir para o meu amigo que se chama Isaque também ter que sempre me fazer uma script em python,então,eu vou fazer essa script por mim mesmo!')
print('Uau professor! Mas você sabe python?')
print('Heeeeeeeeehhhh,não! Kkkkk')
print('Como o senhor vai fazer então?')
print('Vou ver os vídeos do Guanabara! Eles ensinam e fazem com que a gente coloque em prática com os exercícios!Que no caso, esse é o vigésimo exercício!')
print('Uau! Eu também posso participar?')
print('Mas é claro! É só pesquisar Guanabara no YT!')


#Ação!
print('Então sem delongas,vamos começar!             ')
print('n1 = input("Qual o primeiro aluno?")')
print('n2 = input("Qual o segundo aluno?")')
print('n3 = input("Qual o terceiro aluno?')
print('n4 = input("E o quarto aluno?")')
n1 = input(str('Qual o primeiro aluno?'))
n2 = input(str('Qual o segundo aluno? '))
n3 = input(str('Qual o terceiro aluno?'))
n4 = input(str('E o quarto aluno?'))
print('lista = (n1,n2,n3,n4)')
lista = (n1,n2,n3,n4)
print('MisturaDaLista = random.shuffle(lista)')
embaralhar = random.sample(lista, 4)
print('print("O trabalho será apresentado na ordem: ")')
print("O trabalho será apresentado na ordem: ")
print('print(MisturaDaLista)')
print(embaralhar)