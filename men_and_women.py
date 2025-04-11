idade18 = quanthomem = less20 = 0
while True:
    print('-' * 52)
    print('-' * 15, 'Cadastre uma pessoa', '-' * 15)
    print('-' * 52)
    idade = int(input('\033[1:39mIdade?: \033[m'))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('\033[1:39mSexo? [M/F]: \033[m')).upper().strip()
    if idade > 18:
        idade18 += 1
    if sexo == 'M':
        quanthomem += 1
    if idade < 20 and sexo == 'F':
        less20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\033[1:39mVocê quer continuar? [S/N]: \033[m')).strip().upper()
    if continuar == 'N':
        print('Acabou')
        print('-' * 20)
        break
print(f'Foram cadastradas \033[1:36m{idade18}\033[m pessoas com mais de 18 anos.')
print(f'Foram cadastrados \033[1:36m{quanthomem}\033[m homens!')
print(f'Foram cadastradas \033[1:36m{less20}\033[m mulheres com menos de 20 anos.')
print('-' * 15, 'ACABOU!!', '-' * 15) 
