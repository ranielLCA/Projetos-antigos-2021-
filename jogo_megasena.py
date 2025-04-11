from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('     JOGA NA MEGA SENA')
print('-' * 30)
quantos = int(input('Quantos jogos você quer sortear?: '))
total = 1
while total <= quantos:
    cont = 0
    while True:
        sorteio = randint(1, 60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1
        elif cont >= 6:
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-' * 25, f'Sorteando {quantos} jogos!', '-' * 25)
for i, l in enumerate(jogos):
    i += 1
    print(f'Jogo {i}: {l[:6]}')
    sleep(0.7)
print('-' * 25, '<', 'BOA SORTE!', '>', '-' * 25)
