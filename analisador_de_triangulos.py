print('-='*20)
print('Analisador de Triangulôs')
print('-='*20)
rt = float(input('Digite uma reta: '))
rt2 = float(input('Digite outra reta: '))
rt3 = float(input('Digite outra reta: '))
retas = (rt, rt2, rt3)
if rt2 < rt + rt2 and rt3 < rt2 + rt and rt < rt2 + rt3:
    print('Seus segmentos PODEM formar um triangulô')
else:
    print('\u001B[0;36mSeus segmentos NÃO podem formar um trangulô')