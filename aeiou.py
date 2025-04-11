palavras = ('Mahito', 'itadori', 'Nobara', 'Fushiguro', 'Gojo', 'Sukuna')
for p in palavras:
    print(f'\nNa Palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')