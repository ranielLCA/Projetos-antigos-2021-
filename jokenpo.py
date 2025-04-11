import random

print('-=' * 10)
print('Jokenpô')
print('-=' * 10)
iitens = 'Pedra', 'Papel', 'Tesoura'
pcjog = (random.randint(0, 3))
print('''Suas jogadas podem ser:
[1] Pedra
[2] Tesoura
[3] Papel''')
playerjog = int(input('Qual sua jogada?: '))
print('-=' * 10)
print('O computador está pensando')
print('-=' * 10)
if pcjog == playerjog:
    print('Empate!')
if pcjog == 0:
    print('Jogada Inválida!')
if pcjog == 1 and playerjog == 2:
    print('Pedra vence papel! \033[4:31mComputador Vence!')
elif pcjog == 2 and playerjog == 1:
    print('Tesoura vence papel! \033[4:33mPlayer Vence!')
elif pcjog == 3 and playerjog == 1:
    print('Tesoura vence papel! \033[4:33mPlayer Vence!')
elif playerjog == 2 and pcjog == 3:
    print('Tesoura vence papel! \033[4:31mComputador Vence!')
elif playerjog == 1 and pcjog == 3:
    print('Papel vence pedra! \033[4:31mComputador Vence!')
elif playerjog == 1 and pcjog == 2:
    print('Pedra vence tesoura! \033[4:31mComputador vence!')