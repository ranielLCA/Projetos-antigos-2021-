matriz = [[], [], []], [[], [], []], [[], [], []]
somacoluna = somapar = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 ==0:
            somapar += matriz[l][c]
    print()
print('-' * 25)
print(f'A soma dos valores pares é {somapar}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
maxmatriz = max(matriz[1][c])
print(f'A soma dos valores da terceira coluna é: {somacoluna}')
for c in range(0, 3):
    if c == 0: 
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')