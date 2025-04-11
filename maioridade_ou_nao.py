somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('\033[1:39m Nome:\033[m '))
    idade = int(input('\033[1:39m Idade:\033[m '))
    sexo = str(input('\033[1:39m Sexo [M/F]:\033[m '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A Méida de idade do grupo é {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'A Quantidade de mulheres com menos de 20 anos é {totmulher20}')