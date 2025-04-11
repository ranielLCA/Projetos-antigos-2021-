valores = (int(input('Número: ')),
           int(input('Número: ')),
           int(input('Número: ')),
           int(input('Número: ')))
print(f'O valor 9 apareceu {valores.count(9)} vez(es)')
print('os valores digitados foram:', end='')
if 3 in valores:
    print(f'O valor 3 está na posição {valores.index(3) + 1}')
else:
    print('Não há o número 3 nos valores sorteados')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')