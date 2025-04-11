lista = [[], []]
valor = 0
for v in range(1, 8):
    valor = int(input(f'Digite o {v}° número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)
print('-' * 25)
print(f'A lista par é:\n'
      f'{lista[0]}')
print('-' * 25)
print(f'E a lista Ímpar é:\n'
      f'{lista[1]}')
print('-' * 25)