from datetime import date

print('Qual o seu sexo?:')
print('Por favor digite [1] para Masculino; e [2] para feminino.')
answer = int(input('\033[1:34m : '))
if answer > 2:
    print('Por favor digite o número [1] ou [2].')
if answer == 1:
    atual = date.today().year
    born = int(input('Em que ano você nasceu?: '))
    idade = atual - born
    if answer == 1:
        print(f'Quem nasceu em {born} tem {idade} anos em {atual}.')
        if idade == 18:
            print(f'\033[1:33m Que você já tem {idade}!? Já está na hora de se alistar!')
        elif idade < 18:
            print(f'\033[1:32m Hã? Você ainda tem {idade} anos?, calma, ainda não está na hora. Seu alistamentos será '
                  f'em {born + 18}')
        elif idade > 18:
            print(f'\033[1:31m Que!? Você já tem {idade} anos!?, Você deveria ter se alistado em {idade - 18} ano(s) Já'
                  f'passou da hora de se alistar!')
if answer == 2:
    print('\033[1:32m Você é mulher, e não precisa se alistar.')