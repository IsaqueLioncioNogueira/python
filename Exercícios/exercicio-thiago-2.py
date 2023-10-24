# 1. Crie um programa que simula uma loja de RPG
# 2. O programa lista 3 itens que tem à venda:
# Espada > 100g
# Escudo > 50g
# Arco > 75g


# O usuario define o ouro que começa. Entao, ele deve selecionar quais itens deseja comprar e a quantidade de cada.
# Ao final, caso o jogador possua ouro suficiente, a loja deve imprimir o seguitne relatorio:

# Espadas: 1x - total: 100g
# Escudos: 2x - total: 100g
# Arcos: 3x - total: 225g
# Total final: 425g

# No entanto, se o jogador nao possuir ouro suficiente, a loja deve imprimir:
# Nao foi possivel comprar os itens! O jogador possui 150g, mas o valor total da compra é 200g!
print('-----------------------------LOJA DO RPG DO ISAQUE-----------------------------')
print('O valor da espada é 100g.')
print('O valor do escudo é 50g.')
print('O valor do arco é 75g')
Ouro = int(input('Digite a quantia de ouro que você começa: '))
VendaDeEspada = int(input('Digite 1 para comprar apenas uma espada e 2 para selecionar a quantia de espadas você deseja comprar: '))
if VendaDeEspada == 2 :
    VendaDeEspada = int(input('Digite o tanto de espadas você quer comprar: '))
VendaDeEscudo = int(input('Digite 1 para comprar apenas um escudo e 2 para selecionar a quantia de escudos você deseja comprar: '))
if VendaDeEscudo == 2 :
    VendaDeEscudo = int(input('Digite o tanto de escudos você quer comprar: '))
VendaDeArco = int(input('Digite 1 para comprar apenas um arco e 2 para selecionar a quantia de arcos você deseja comprar: '))
if VendaDeArco == 2 :
    VendaDeArco = int(input('Digite o tanto de arcos você quer comprar: '))
TotalDeTudo = VendaDeArco*75 + VendaDeEscudo*50 + VendaDeEspada*100
if TotalDeTudo < Ouro :
    print('Arcos:',VendaDeArco,'total:',VendaDeArco*75,
          'Espadas:',VendaDeEspada,'total:',VendaDeEspada*100,
          'Escudos: ',VendaDeEscudo,'total:',VendaDeEscudo*50)
else :
    print('No foi possivel comprar os itens! O jogador possui ',Ouro,'g mas o valor total da compra é ',TotalDeTudo,'g!')