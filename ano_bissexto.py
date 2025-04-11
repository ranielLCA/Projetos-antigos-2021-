import calendar
ano = int(input('Digite o ano: '))
ano6 = calendar.isleap(ano)
if ano6 is True:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')