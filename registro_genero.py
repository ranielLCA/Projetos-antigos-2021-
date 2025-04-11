s = str(input('\033[0:39mDigite seu sexo\033[m \033[1:39m[M/F]\033[m:')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('\033[1:31mValor Inválido! Por Favor digite novamente:\033[m \033[1:39m[M/F]\033[m:')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso')