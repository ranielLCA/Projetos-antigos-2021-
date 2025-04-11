print('Considere os valores colocados em tamanho calculados em \033[1:39mMetros.')
r1 = float(input('Digite o tamanho de um dos lados: '))
r2 = float(input('Digite o tamanho de um dos lados: '))
r3 = float(input('Digite o tamanho de um dos lados: '))
if r1 < r2 + r3 and r3 < r2 + r1 and r2 < r3 + r1:
    print('Seus lados podem formar um triãngulo!')
    if r1 == r2 == r3:
     print('Podem foramr um \033[4:34mTriângulo Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Seus lados podem formar um \033[4:35mTriângulo Escaleno!')
    else:
        print('Seus lados podem formar um \033[4:38mTriângulo Isósceles')
else:
    print('Seus lados não podem fazer um triângulo!')