totgasto = produtoalto = menor = cont = 0
barato = ''
while True:
    print('\033[1:39m⇨ ', 'ÁNALISE DE DADOS DO MERCADINHO DO ZÉ!', '⇦ \033[m')
    produto = str(input('Produto?: '))
    preco = float(input('Qual o preço do produto? | R$:'))
    cont += 1
    totgasto += preco
    if preco > 1000:
        produtoalto += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar?: ')).upper().strip()[0]
    if continuar == 'N':
        break
    print(f'O Total gasto foi \033[1:32m{totgasto:.2f}\033[m')
    print(f'Haviam {produtoalto} produto(s) acima de R$1.000. ')
    print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')