peso = float(input('Digite seu peso (KG): '))
altura = float(input('DIgite sua altura (m): '))
IMC = peso / (altura ** 2)
if IMC > 18.5:
    print(f'Você tem o IMC de {int(IMC)} e está \033[4:33mAbaixo\033[1:33m do Peso.')
elif 18.5 > IMC <= 25:
    print(f'Você tem o IMC de {int(IMC)} e está no peso \033[4:34mIdeal.')
elif 25 > IMC <= 30:
    print(f'Você tem o IMC de {int(IMC)} e está com \033[4:38mSobrePeso.')
elif 30 > IMC <= 40:
    print(f'Você tem o IMC de {int(IMC)} e está com \033[4:35mObesidade.')
elif IMC >= 40:
    print(f'Você tem o IMC de {int(IMC)} e está/Tem \033[4:36mObesidade Mórbida.')