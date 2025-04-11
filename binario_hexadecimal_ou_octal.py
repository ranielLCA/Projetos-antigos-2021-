print('\033[1:34m[1] Para Binário')
print('\033[1:33m[2] Para Octal')
print('\033[1:32m[3] Para Hexadecimal')
ne = int(input('\033[1:39m Digite o conversor: '))
n = float(input('Digite um número: '))
no = oct(n)
nn = ((((n / 2) // 2) / 2 // 2 / 2 // 2))
nh = hex(n)
if ne == 1:
    print(f'O número {n} em binário é {nn}')
elif ne == 2:
    print(f'O número {n} em Octal é {no}')
elif ne == 3:
    print(f'O número {n} em Hexadecimal é {nh}')