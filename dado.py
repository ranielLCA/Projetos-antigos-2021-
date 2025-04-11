from random import randint
from time import sleep
from operator import itemgetter
dado = {'Jogador 1:': randint(1, 6),
        'Jogador 2:': randint(1, 6),
        'Jogador 3:': randint(1, 6),
        'Jogador 4:': randint(1, 6),
        }
rank = []
print(f'O dado vai rolar!')
sleep(0.7)
for keys, values in dado.items():
    print(f'O Jogador {keys} tirou o número {values}.')
    print(dado.items())
    sleep(0.7)
rank = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('-' * 35)
for itens, values in enumerate(rank):
    print(f'{itens}° lugar: {values[0]} com {values[1]}')
    sleep(0.7)