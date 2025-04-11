import random
print('===   Jogo da adivinhação      ===  ')
print('=======     Pensando. . .    =======')
r = random.randint(10, 20)
ni = int(input('tente adivinhar otário kkkkkkkkkk: '))
if ni == r:
    print('Caralho menó, como que você acertou? Tá virando o Akinator é?')
else:
    print(f'errou otáriokkkkkkkkkkkkkkkkk, eu pensei em {r}')