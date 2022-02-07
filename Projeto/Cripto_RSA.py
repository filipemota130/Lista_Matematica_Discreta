cripto = []
p = q = n = d = e = 0

def mod_power(a, exp, mod):
        r=1
        while exp>0:
            if exp & 1 == 1:
                r= (r*a) % mod
            a = (a*a)%mod
            exp>>=1
        return r
    
def key_gen():
    def eh_primo(n):
        for p in range(2, n//2):
            if n % p == 0:
                return 1
        return 0
    
    def euclides(A, D):
        while D != 0:
            aux = D
            D = A % D
            A = aux    
        return A

    while True:
        p=int(input("\n#1 insira um numero primo: ")) #Primeiro primo 'p'
        q=int(input("#2 insira um numero primo: ")) #Segundo primo 'q'
        if(p<2 or q<2 or eh_primo(p)!=0 or eh_primo(q)!=0):
            print("  Valores inválidos, não são primos!")
        else:
            print("  Valores válidos!")
            break
            
    n=p*q #Valor de N
    relativo=(p-1)*(q-1) #Função totiente de N = φ(x)

    while True:
        e = int(input(f'\nInsira um valor entre 1 e {relativo}, que seja relativamente primo a {relativo}: '))
        eh_coprimo = euclides(e, relativo)
        if eh_coprimo == 1:
            print("Sua chave foi gerada!")
            print("Você pode encontra-la no arquivo key.txt gerado na pasta atual")
            break
        else:
            print('Valor inválido!')

    with open("key.txt", "w") as f:
        f.write('Essas sao as suas chaves publicas:\n')
        f.write(f'Chave N: {n}\n')
        f.write(f'Chave E: {e}\n')

def criptografando_msg():
    
    global cripto
    msg = str(input('\nDigite a mensagem que deseja criptografar: ')).strip().lower()
    criptografada = list()
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

    for t in criptografada:
        c = mod_power(t,e,n)
        cripto.append(c)

    cripto = str(cripto)
    cripto = cripto.replace("[","")
    cripto = cripto.replace("]","")
    cripto = cripto.replace("\n","")
    cripto = cripto.replace(",","")
    
    with open("criptografada.txt", "w") as f:
        f.write(cripto)
    print("\nMensagem criptografada!!")

    
def desencritando():
    
    def inversoMod(e, relativo, b):
        while b < relativo:
            if e * b % relativo == 1:
                return b
            else:
                b+=1

    with open("criptografada.txt", "r") as f:
        line= f.readlines()
    cripto = line[0]
    cripto = cripto.replace("[","")
    cripto = cripto.replace("]","")
    cripto = cripto.replace("\n","")
    cripto = cripto.replace(","," ")
    cripto = cripto.split(" ")
    cripto = list(map(int, cripto))

    p = int(input('\nDigite a chave P: '))
    q = int(input('Digite a chave Q: '))
    e = int(input('Digite a chave E: '))

    print("\nDesencriptando...")
    n=p*q #Valor de N
    relativo=(p-1)*(q-1) #Função totiente de N = φ(x)

    d = inversoMod(e, relativo, 1)

    descriptografada = list()
    for c in cripto:
        t = mod_power(c, d, n)
        descriptografada.append(t)

    desen = list()
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
    print("\nDesencriptação Concluida!!")
    print('\nA mensagem foi:')
    print('"', end='')
    for p in desen:
        print(f'{p}', end='')
    print('"', end='')

print('\nPROGRAMA DE CRIPTOGRAFIA')
while True:
    print('\n\n    [ 1 ] Gerar uma chave Pública\n    [ 2 ] Encriptar Mensagem\n    [ 3 ] Desencriptar Mensagem\n    [ 0 ] Encerrar Programa')
    resp = int(input('\nDigite a opção que deseja executar: '))
    if resp == 0:
        break
    elif resp == 1:
        key_gen()
    elif resp == 2:
        criptografando_msg()
    elif resp == 3:
        desencritando()