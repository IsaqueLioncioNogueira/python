# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
# À Vista dinheiro/cheque, 10% de desconto
# À vista no cartão 5% de desconto
# Em até 2 x cartão, preço normal
# 3x ou mais no cartão, 20% de juros
n1 = float(input('Digite o valor do produto: '))
n2 = int(input('Agora,digite 1 para á vista no dinheiro ou cheque,2 para á vista no cartão,3 para em até 2x no cartão,4 para 3x ou mais no cartão'))
n3 = n1 / 100
if n2 == 1 :
    print('O novo valor do produto com desconto é:',n3 * 90)
elif n2 == 2 :
    print('O novo valor do produto com desconto é:',n3 * 95)
elif n2 == 3:
    print('O novo valor do produto com desconto é:',n3 * 100)
elif n2 == 4 :
    print('O novo valor do produto com desconto é:',n3 * 120)