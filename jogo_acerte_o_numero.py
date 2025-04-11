import random
import time
pc = random.randint(0, 10)
print('-=' * 15)
print('''Estou pensando em um número de 0 até 10 e vou contar até cinco pra você pensar sobre qual é, você consegue adivinhar qual é?
''')
time.sleep(5)
print('\033[1:39mTEMPO ESGOTADO!\033[m')
print('-=' * 15)
player = int(input('Qual número você pensou que eu pensei?:'))
while player != pc:
    player = int(input('\033[1:31mERROU!\033[m \033[0:33mTente Novamente!:\033[m '))
if player == pc:
    print('\033[1:32mACERTOU!\033[m')
