# Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: Todos os lados diferentes
num1 = float(input('Digite o tamanho da primeira reta: '))
num2 = float(input('Digite o tamanho da segunda reta: '))
num3 = float(input('Digite o tamanho da terceira reta: '))
num4 = num1 / 3
if num1 == num2 and num1 == num3 :
    print('Dá para você formar um triângulo equilátero!')
elif num1 == num2 or num3 == num2 :
    print ( 'Dá para você formar um triângulo isóceles!' )
elif num1 != num2 and num1 != num3 :
    print ( 'Dá para você formar um triângulo escaleno!' )