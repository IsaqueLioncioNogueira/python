# Exercicio RPG
# 1. O programa deve ler a vida e a defesa de um jogador
# 2. O programa em seguida deve solicitar um numero que representa o ataque que esse jogador recebera
# 3. O programa exibe uma mensagem na tela como a seguinte:
# O jogador tem 10 de vida e defesa 5. Ao receber 10 de ataque, sofrerá 5 dano. Agora o jogador tem 5 de vida.
NomeDoPlayer = str(input('Digite o nome de seu personagem: '))
print('A vida limite do(a) ',NomeDoPlayer,'pode ser, no máximo 20 de vida.')
VidaDoPlayer = int(input('Digite a vida do seu personagem: '))
while VidaDoPlayer > 20:
    VidaDoPlayer = int(input('Digite a vida do seu personagem: '))
print('Mas, a defesa máxima do(a)',NomeDoPlayer,'pode ser infinita!')
DefesaDoPlayer = int(input('Agora, digite a defesa de seu player'))
TotalDeVidaAGastar = VidaDoPlayer + DefesaDoPlayer
Dano = int(input('Agora, digite o dano que voce vai dar em seu personagem: '))
DefesaAGastar = DefesaDoPlayer-Dano
print('O ',NomeDoPlayer,' tem ',VidaDoPlayer,' de vida e defesa',DefesaDoPlayer,' Ao receber ',Dano,' de ataque, sofrerá ',DefesaAGastar*-1,'de dano. Agora o jogador tem ',TotalDeVidaAGastar-Dano,' de vida.')