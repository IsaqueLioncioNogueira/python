# Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez
frase = str(input('Digite uma frase qualquer: ')).upper().strip()
letra = str(input('Digite a letra que quer analisar: ')).upper().strip()

print(f'A letra ',letra,' apareceu ',frase.count(letra),' vezes')
print(f'A primeira aparição da letra ',letra,' foi na ',frase.find(letra)+1,'°a posição ')
print(f' a última vez que a letra ',letra,' apareceu foi na ',frase.rfind(letra)+1,'°a posição')