# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final mostre:
# Média de idade do grupo
# Nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
n2 = 0
#Primeira questão:
nome1 = str(input('Digite o nome de uma pessoa: '))
idade1 = int(input('Digite a idade dela: '))
sexo1 = int(input('Digite o sexo dela: "1" para homem e "2" para mulher: '))
nome2 = str(input('Digite o nome de uma pessoa: '))
idade2 = int(input('Digite a idade dela: '))
sexo2 = int(input('Digite o sexo dela: "1" para homem e "2" para mulher: '))
nome3 = str(input('Digite o nome de uma pessoa: '))
idade3 = int(input('Digite a idade dela: '))
sexo3 = int(input('Digite o sexo dela: "1" para homem e "2" para mulher: '))
nome4 = str(input('Digite o nome de uma pessoa: '))
idade4 = int(input('Digite a idade dela: '))
sexo4 = int(input('Digite o sexo dela: "1" para homem e "2" para mulher: '))
n1 = (idade1+idade2+idade3+idade4)/4
print('A média da idade do grupo é:',n1)
#Fim da primeira questão...

#Segunda questão:
if sexo1 == 1 and idade1 > idade2 and idade1 >idade3 and idade1 >idade4 :
    print('O',nome1,'é o homem mais velho!')
if sexo2 == 1 and idade2 > idade3 and idade2 >idade4 and idade2 > idade1:
    print('O',nome2,'é o homem mais velho!')
if sexo3 == 1 and idade3 > idade4 and idade3>idade2 and idade3> idade1:
    print('O',nome3,'é o homem mais velho!')
if sexo4 == 1 and idade4 > idade2 and idade4 > idade3 and idade4 > idade1 :
    print('O',nome4,'é o homem mais velho!')
#Fim da segunda questão...

#Terceira questão:
if sexo1 == 2 and idade1 < 20:
    n2 += 1
if sexo2 == 2 and idade2 < 20:
    n2 += 1
if sexo3 == 2 and idade3 < 20:
    n2 += 1
if sexo4 == 2 and idade4 < 20:
    n2 += 1
print(n2,'mulheres tem menos de 20 anos!')