from datetime import date
hoje = date.today().year
born = int(input('Quando você nasceu?:\033[1:34m '))
idade = hoje - born
if idade <= 9:
    print(f'Você tem {idade} anos, você é um competidor \033[4:33mMirim!')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos, então você é um competidor \033[4:34mInfantil!')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos, então você é um competidor \033[4:35mJunior!')
elif 19 < idade <= 20:
    print(f'Você tem {idade} anos, então você é um competidor \033[4:38mSênior!')
elif idade >= 20:
    print(f'Você tem {idade} anos, então você é um comeptidor \033[4:39mMaster!')