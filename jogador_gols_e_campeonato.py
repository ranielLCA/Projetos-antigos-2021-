dadosfutebol = {}
partidas = []
dadosfutebol['Nome'] = str(input('Nome do jogador: '))
PARTIDAS = (int(input('Quantidade de partidas jogadas: ')))
for c in range(1, PARTIDAS + 1):
    partidas.append(int(input(f'Quantos gols ele fez na partida {c}?: ')))
dadosfutebol['Gols'] = partidas[:]
print('-' * 30)
print(f'INFORMAÇÕES SOBRE O JOGADOR ->')
print(dadosfutebol)
print('-' * 30)
print(f"O jogador se chama {dadosfutebol['Nome']};")
print(f"Os gols de {dadosfutebol['Nome']} foram {dadosfutebol['Gols']};")
print(f"E a quantidade de gols totais que {dadosfutebol['Nome']} fez no campeonato é {sum(partidas)} ")
print(f'-' * 30)
print(f"O jogador {dadosfutebol['Nome']} jogou {partidas} partidas")
for c in range(1, PARTIDAS + 1):
    print(f"---> Na Partida {c}, {dadosfutebol['Nome']} fez {partidas} gols")
print(f'Com um total de {sum(partidas)} gols.')