print('=' * 25)
print('       BANCO DO ZÉ     ')
print('=' * 25)
valor = int(input('Qual o valor a ser sacado?: '))
total = valor
cedula = 50
ttced = 0
while True:
    if total >= cedula:
        total -= cedula
        ttced += 1
    else:
        if ttced > 0:
            print(f'Total de {ttced} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        ttced = 0
        if total == 0:
            break