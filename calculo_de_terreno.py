def area(largura, comprimento):
    resultado = largura * comprimento
    print(f'O Terreno com {l} largura, e {c} de comprimento, tem {resultado}m² de área.\n'
          f'Ou {largura}x{comprimento} tem {resultado} de m².')


def linhatxt():
    print('-' * 30)


linhatxt()
print('     Cálculo De Terrenos ')
linhatxt()
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M):  '))
area(l, c)