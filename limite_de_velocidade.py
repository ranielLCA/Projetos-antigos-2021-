kmr = float(input('Qual a velôcidade que você estava dirigindo?: '))
kmu = (kmr - 80) * 7.00
if kmr > 80:
    print(f'Você ultapassou o limite de velocidade (80km/h), você vai ser multado em R${kmu}')
else:
    print('Você dirigiu normalmente e sem quebrar nenhum limite de velocidade, parabéns!')