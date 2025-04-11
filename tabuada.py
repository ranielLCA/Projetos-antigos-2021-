while True:
    print('\033[1:39m-=' * 15, 'TABUADA', '=-' * 15)
    num = int(input('''Escolha um número e lhe mostraremos a sua tabuada (Até a décima multipliacação.) 
    independentemente de qual seja! (Caso queira parar digite um valor negativo.) 
    Digite o número da tabuada: \033[m'''))
    if num < 0:
        print('\033[1:31mNúmero Negativo Digitado!\033[m')
        print('\033[1:39m-=' * 10, 'ENCERRANDO PROGRAMA', '-=' * 10)
        break
    x1 = num * 1
    x2 = num * 2
    x3 = num * 3
    x4 = num * 4
    x5 = num * 5
    x6 = num * 6
    x7 = num * 7
    x8 = num * 8
    x9 = num * 9
    x10 = num * 10
    print(f'-=' * 15, 'AQUI ESTÀ Á TABUADA!', '-=' * 15)
    print(f'''
    {num} * 1 = \033[1:39m{x1}\033[m
    {num} * 2 = \033[1:39m{x2}\033[m
    {num} * 3 = \033[1:39m{x3}\033[m
    {num} * 4 = \033[1:39m{x4}\033[m
    {num} * 5 = \033[1:39m{x5}\033[m
    {num} * 6 = \033[1:39m{x6}\033[m
    {num} * 7 = \033[1:39m{x7}\033[m
    {num} * 8 = \033[1:39m{x8}\033[m
    {num} * 9 = \033[1:39m{x9}\033[m
    {num} * 10 = \033[1:39m{x10}\033[m''')
    print('-' * 10, 'REINICIANDO PROGRAMA', '-' * 10)