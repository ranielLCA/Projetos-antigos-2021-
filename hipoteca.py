hp = str(input('Qual o valor da casa?: ' ))
pagar = int(input('Em quantos anos você quer pagar a casa?: '))
qoh = str(input('Você quer comprar uma casa? (por favor digite sim ou não.): '))
salário = int(input('Qual o valor do seu salário?: '))
parcela = salário * 30 / 100
if qoh == 'sim':
    print('muito bem, vamos lá! NOTA: Tenha em mente que se a parcela da casa for maior que seu salário, o senhor(a) não poderá fazer a compra.')
elif salário > parcela:
    print('Vamos ao acordo, o senhor pode comprar a casa!')
elif parcela > salário:
    print('O senhor não pode comprar a casa, pois seu salário não pode pagar por ela.')
else:
    print('Oh, muito bem. Nos procure quando tiver interesse.')