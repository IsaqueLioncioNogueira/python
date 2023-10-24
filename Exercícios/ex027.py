# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separados
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza
nome = str(input('Digite seu nome: ')).strip()
divisao = nome.split()
print(f"""Muito prazer em te conhecer!
Seu primeiro nome é {(divisao[0])}
Seu ultimo nome é {(divisao[-1])}.""")