n = int(input('\033[1:34m Digite um número: '))
n2 = int(input('\033[1:34m Digite mais um número: '))
if n < n2:
    print(f'O número {n2} é maior que o {n}, e \033[1:35m o número {n} menor que o número {n2}. ')
elif n2 > n:
    print(f'O número {n} é maior que o número {n2}, sendo o número \033[1:32m{n2} menor.')
elif n2 == n:
    print('Os dois números são \033[1:34miguais!')