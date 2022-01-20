msg = str(input('\nDigite a mensagem que deseja criptografar: ')).strip().lower()
list(msg)
criptografada = list()
cripto = list()
for m in msg:
    if m == 'a':
        m = 2
    elif m == 'b':
        m = 3
    elif m == 'c':
        m = 4
    elif m == 'd':
        m = 5
    elif m == 'e':
        m = 6
    elif m == 'f':
        m = 7
    elif m == 'g':
        m = 8
    elif m == 'h':
        m = 9
    elif m == 'i':
        m = 10
    elif m == 'j':
        m = 11
    elif m == 'k':
        m = 12
    elif m == 'l':
        m = 13
    elif m == 'm':
        m = 14
    elif m == 'n':
        m = 15
    elif m == 'o':
        m = 16
    elif m == 'p':
        m = 17
    elif m == 'q':
        m = 18
    elif m == 'r':
        m = 19
    elif m == 's':
        m = 20
    elif m == 't':
        m = 21
    elif m == 'u':
        m = 22
    elif m == 'v':
        m = 23
    elif m == 'w':
        m = 24
    elif m == 'x':
        m = 25
    elif m == 'y':
        m = 26
    elif m == 'z':
        m = 27
    elif m == ' ':
        m = 28
    criptografada.append(m)

n = int(input('\nDigite o valor de N obtido no programa passado: '))
e = int(input('Digite o valor de E escolhido no programa passado: '))

for c in criptografada:
    c = c**e % n
    cripto.append(c)

with open("criptografada.txt", "w") as f:
    f.write(f'Sua mensagem criptografada está aqui:\n{cripto}\n')