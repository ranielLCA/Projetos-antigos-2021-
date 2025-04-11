soma = 0
cont = +1
for c in range(1, 501, 2):
    if c % 3 == 0:
     soma = soma + c
     cont = cont + 1
print(f'''O resultado da soma entre os todos números divísiveis ({cont}) por 3 até 500 é :'
              \033[4:32m{soma + c}''')