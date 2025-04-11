casa = float(input('Qual o valor da casa?: '))
salário = float(input('Qual o seu salário?: '))
anos = int(input('Em quantos anos você quer pagar a casa?: '))
minímo = (salário * 30) / 100
prestação = casa / (anos * 12)
print('Comparando o preço da prestação com seu salário. . . .')
if prestação <= minímo:
    print('O empréstimo\033[1:34m pode ser concedido!')
else:
    print('O empréstimo não pode ser concedido, pois seu salário não cumpre os 30% necessários para pagá-lo.')