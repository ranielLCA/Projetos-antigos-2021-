print('=-' * 15)
print('     TABELA DO BRASILEIRÃO    ')
print('=-' * 15)
tabela = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', \
    'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceára', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná'
print('-' * 13, 'INFORMAÇÕES ABAIXO  ↓')
print(f'\033[1:32mCinco primeiros da colocação\033[m são: \n' 
      f'{tabela[0:5]}')
print('-' * 12)
print(f'Os \033[1:31múltimos quatro colocados\033[m são:\n'
      f'{tabela[-4:]}')
print('-' * 12)
print(f'A lista em \033[1:34mordem alfabética\033[m é: \n'
      f'{sorted(tabela)}')
print('-' * 12)
print(f'A CHapecoense está na posição :\n{tabela.index("Chapecoense") + 1}°')