def linhatxt():
    print('-' * 30)


def escreva(txt):
    linhatxt()
    print(f'{txt:>15}')
    linhatxt()


txt = str(input('Qual o seu texto?: '))
escreva(txt)