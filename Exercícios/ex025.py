# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nam = str(input('Digite um nome: ')).strip()
print(nam[:5].upper() == 'SILVA')