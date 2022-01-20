criptografada = [145, 194, 31, 88, 200, 109, 31, 57, 36, 194, 43, 145, 109, 31, 216, 194, 6, 107, 43, 6]
d = int(input('\nDigite a chave D: '))
n = int(input('Digite a chave N: '))
descriptografada = list()
for c in criptografada:
    c = c**d % n
    descriptografada.append(c)

desen = list()
resp = str(input('\nDeseja desencriptala? [Y/N] ')).strip().upper()
if resp == 'Y':
    for m in descriptografada:
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
print('\nA mensagem foi:\n')
for p in desen:
    print(f'{p}', end='')