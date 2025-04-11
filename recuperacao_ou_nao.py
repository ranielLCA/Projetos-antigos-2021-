Nota1 = float(input('\033[1:39mDigite uma nota: '))
Nota2 = float(input('\033[1:39mDigite outra nota: '))
mediaa = (Nota2 + Nota1) / 2
if mediaa > 7.0:
    print(f'Muito bem! Sua média foi de \033[1:39m {mediaa}, você foi \033[4:32maprovado!')
elif mediaa > 5 and 6:
    print(f'Sua média foi \033[1:39m{mediaa}, estude mais e você ficará de \033[4:33mrecuperação!')
elif mediaa <=4.9:
    print(f'\033[1:39mVocê tirou uma nota muito baixa! Sua média foi de {mediaa}. Você foi \033[4:31mreprovado!')