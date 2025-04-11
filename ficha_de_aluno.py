ficha  = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, nota1, nota2, media])
    continuar = str(input('Quer continuar?: '))
    if continuar in 'Nn': 
        break
print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-' * 25)
for i, a in enumerate(ficha): 
    print(f'{i:<4}{a[0]:>10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar as notas de qual aluno? (999 Para o programa): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1: 
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<   VOLTE SEMPRE  >>')