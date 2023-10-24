# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras em maiúsculas
# O nome com todas minúsculas
# Quantas letras no total (sem considerar espaços)
# Quantas letras tem o primeiro nome
print('Isaque.GPT:')
name = str(input('Digite um nome: '))
print('De acordo.... com os ..... meus cál...culos, vou ... te mostr..ar todas as.. informaçõs ... que eu achei.: ')
print('O seu name em letras maiúsculas',name.upper())
print('O seu name em letras minúsculas',name.lower())
print('Your nome tem in total ',len(name) - name.count(' '))
cut = name.split()
print('In seu primeiro no...me tem',len(cut[0]),'letras, e o nome que você escreveu é o: ',cut[0])