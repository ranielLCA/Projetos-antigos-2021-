num1 = int(input('Valor(?): '))
num2 = int(input('Valor(?): '))
num3 = int(input('Valor(?): '))
num4 = int(input('Valor(?): '))
num5 = int(input('Valor(?): '))
tot = 0
numeros = num1, num4, num5, num3, num2
menor = min(numeros)
maior = max(numeros)
media = (num1 + num2 + num3 + num4 + num5) / 2
print(f'O Maior valor é {maior}, o Menor ´{menor}.'
      f'A Média Final entre os números é {media}')
conti = str(input('Quer continuar?[S/N]: ')).upper().strip()
while conti != 'N':
    num1 = int(input('Digite o valor novamente: '))
    num2 = int(input('Digite o valor novamente: '))
    num3 = int(input('Digite o valor novamente: '))
    num4 = int(input('Digite o valor novamente: '))
    num5 = int(input('Digite o valor novamente: '))
    tot += 1
    media = tot / 2
    numeros = num1, num4, num5, num3, num2
    maior = max(numeros)
    menor = min(numeros)
    print(f'O Maior valor é {maior}, o Menor {menor}.'
          f'A Média Final entre os números é {media}')
    conti = str(input('Quer continuar?[S/N]: ')).upper().strip()
print('-=-=-=-=-=-=-=-=-=-=- OBRIGADO POR USAR NOSSO PROGRAMA!  =-=-=-=-=-=-=-=-=-=-=-=-=-')