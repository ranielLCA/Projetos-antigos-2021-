from random import randint
from time import sleep

print('\033[1:30m=-=\033[m' * 10)
print('\033[1:39m    JOGO DO PAR OU ÍMPAR!      \033[m')
print('\033[1:30m=-=\033[m' * 10)
while True:
    player = int(input('Qual seu número escolhido?: '))
    pc = randint(0, 11)
    resultado = player + pc
    victory = 0
    tipo = ' '
    while tipo not in 'PpIi':
        print('-' * 20)
        tipo = str(input('Par Ou ìmpar [P/I]?: ')).strip().upper()
        print('-' * 20)
    print(f'Você jogou \033[1:32m{player}\033[m e o computador \033[1:36m{pc}\033[m e deu \033[1:39m{resultado}\033[m')
    print('=-=' * 15)
    if tipo == 'P':
        if resultado % 2 == 0:
            print('\033[1:32mVocê Venceu!\033[m')
            victory = + 1
            print('PARTIDA GANHA!!')
            print('=-=' * 15)
            print('Reiniciando em 5 segundos. . .')
            print('=-=' * 15)
            print(sleep(5))
        else:
            break
    if tipo == 'I':
        if resultado % 3 <= 1:
            print(f'\033[1:39mVocê Perdeu!\033[m')
            break
print(f'\033[4:31mG A M E   O V E R\033[m e você venceu \033[1:36m{victory}\033[m vezes.')