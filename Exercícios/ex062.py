# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
termo = int(input('Digite um termo: '))
print(termo)
while termo != 0:
    termo = int(input('Digite 0 para encerrar o programa ou digite um termo qualquer: '))
    print(termo)
print('------------------------------------FIM DO PROGRAMA------------------------------------')