sal = float(input('Digite o seu salário: '))
sala = (sal * 10) / 10
if sal < 1250.00:
    sala = ((sal * 15) / 100) + sal
else:
    sala = ((sal * 10) / 100) + sal
print(f'Seu novo salário  é R${sala}')