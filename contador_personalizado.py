from time import sleep
def linhatxt():
    print('-' * 30)


def escreva(txt):
    linhatxt()
    print(f'{txt:>15}')
    linhatxt()


def contador(ínicio, fim, pulando):
    print(f'Contagem de {ínicio} até {fim} de {pulando} em {pulando}.')
    sleep(1.5)
    linhatxt()
    if ínicio < fim:
        cont = ínicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += pulando
        print('FIM!')
    else:
        cont = ínicio
        while ínicio >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= pulando
            if cont == 0:
                break
        print('FIM!')


txt = 'Contador!'
escreva(txt)
linhatxt()
contador(1, 10, 1)
linhatxt()
contador(10, 0, 2)
linhatxt()
txt = 'Agora é sua vez de personalizar o contador!'
escreva(txt)
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Pulando: '))
contador(i, f, p)
escreva('FIM')