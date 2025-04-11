def maior(*num):
    max(num)
    linhatxt()
    print(f'Os números são {num} e Foram informados {len(num)} valores.')
    print(f'O maior valor informado é {max(num)}')
    linhatxt()

def linhatxt():
    print(f"-----------------------")



linhatxt()
maior(1, 9, 10)
maior(8, 10, 90)
maior(45, 2, 8)
maior(0, 1)