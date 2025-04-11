todos = []
dados = {}
cont = 0
mulher = []
acimamedia = []
while True: 
    dados['Nome'] = str(input('Nome: '))
    dados['Idade'] = int(input('Idade: '))
    dados['Sexo'] = str(input('Sexo: '))
    cont += 1
    continuar = ' '
    if continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
todos.append(dados)
média = sum(dados['Idade']) / cont
print('-' * 30)
print(f'Foram cadastradas {cont} pessoas;')
print(f'A média de idade do grupo é: {média}')
if dados['Sexo'] == 'Ff':
    mulher.append()
print(f'As mulheres do grupo são:\n'
      '{mulher}')
if dados['Idade'] > média:
    acimamedia.append()
print(f'As pessoas acima da média são:\n'
      '{acimamedia}')