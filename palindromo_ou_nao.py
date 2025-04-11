frase = str(input('\033[1mDigite a frase\033[m \033[1:39m(Por favor digite em letras maiúsculas)\033[m: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('\033[1:32mPalíndromo\033[m\033[1:39m!\033[m')
else:
    print('\033[1:31mNão é um Palíndromo\033[m\033[1:39m!\033[m')