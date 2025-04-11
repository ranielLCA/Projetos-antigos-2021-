boletim = dict()
print('-' * 15)
boletim['Nome: '] = str(input('Nome: '))
nota1 = float(input('Nota: '))
nota2 = float(input('Nota: '))
média = (nota1 + nota2) / 2
boletim['Média Final: '] = média
if média >= 5:
    boletim['Situação: '] = 'Aprovado!'
elif média < 5:
    boletim['Situação: '] = 'Reprovado!'
print('Situação Final --------')
print(f'{boletim}\n', end=' ')
print()