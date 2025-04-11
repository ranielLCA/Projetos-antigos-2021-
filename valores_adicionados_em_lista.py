num = list()
while True:
    num1 = int(input('Número: '))
    if num1 not in num:
        num.append(num1)
        print('Valor adicionado!')
    else:
        print('Valor já adicionado! Redigite')
    continua = str(input('Quer continuar? [S/N]: '))
    if continua in 'Nn':
        break
print('-' * 45)
num.sort()
print(f'Valores em ordem crescente:\n'
      f'\n{num}\n')
print('-' * 45)