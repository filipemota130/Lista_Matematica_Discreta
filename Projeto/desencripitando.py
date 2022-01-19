criptografada = [17, 19, 16, 11, 6, 21, 16, 28, 4, 19, 10, 17, 21, 16, 8, 19, 2, 7, 10, 2, 28, 19, 20, 2]
desen = list()
resp = str(input('\nDeseja desencriptala? [Y/N] ')).strip().upper()
if resp == 'Y':
    for m in criptografada:
        m = str(m)
        if m == '2':
            m = 'a'
        elif m == '3':
            m = 'b'
        elif m == '4':
            m = 'c'
        elif m == '5':
            m = 'd'
        elif m == '6':
            m = 'e'
        elif m == '7':
            m = 'f'
        elif m == '8':
            m = 'g'
        elif m == '9':
            m = 'h'
        elif m == '10':
            m = 'i'
        elif m == '11':
            m = 'j'
        elif m == '12':
            m = 'k'
        elif m == '13':
            m = 'l'
        elif m == '14':
            m = 'm'
        elif m == '15':
            m = 'n'
        elif m == '16':
            m = 'o'
        elif m == '17':
            m = 'p'
        elif m == '18':
            m = 'q'
        elif m == '19':
            m = 'r'
        elif m == '20':
            m = 's'
        elif m == '21':
            m = 't'
        elif m == '22':
            m = 'u'
        elif m == '23':
            m = 'v'
        elif m == '24':
            m = 'w'
        elif m == '25':
            m = 'x'
        elif m == '26':
            m = 'y'
        elif m == '27':
            m = 'z'
        elif m == '28':
            m = ' '
        desen.append(m)
for p in desen:
    print(f'{p}', end='')