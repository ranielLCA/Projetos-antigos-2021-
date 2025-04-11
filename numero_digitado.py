numeros = 'zero', 'um', 'dois', 'três,' 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte '
while True:
    num = int(input('Diga um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('\033[4:31mVálor Inválido!')
    print('\033[4:32mDigite novamente!\033[m')
print(f'Você digitou o número {numeros[num - 1]}')