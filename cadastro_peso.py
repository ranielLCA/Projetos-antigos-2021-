cont = 0
temporaria = []
principal = []
leve = []
pesada = []
mai = men = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = temporaria[1]
    else:
        if temporaria[1] > mai:
            mai = temporaria[1]
        if temporaria[1] < men:
            men = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    cont += 1
    print('Pessoa cadastrada!')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer Continuar [S/N]: ')).upper().strip()
        if continuar in 'Nn':
            break
    if continuar in 'Nn':
        break
    print('-' * 25)
print('-' * 25)
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi {max(principal)}')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print('')
print(f'E o menor peso foi {min(principal)}', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')