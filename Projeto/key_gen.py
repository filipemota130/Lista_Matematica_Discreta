def coprimo(e, relativo):
    cont = 0
    for p in e:
        for n in relativo:
            if p == n:
                cont+=1
    return cont;

def divisor(n):
    divi = list()
    for p in range(2, n + 1):
        if n % p == 0:
            divi.append(p)
    return divi

def euclides(A,D):
    resto = 1
    while resto>0:
        resto = A % D
        A = D
        D = resto
    return A

def eh_primo(n):
    count = 0
    for p in range(2, n):
        if p % n == 0:
            count += 1
    return count

while True:
    x=int(input("\n#1 insira um numero primo: ")) #Primeiro primo 'p'
    y=int(input("#2 insira um numero primo: ")) #Segundo primo 'q'
    if(x<2 or y<2 or eh_primo(x)!=0 or eh_primo(y)!=0):
        print("valores inválidos, não são primos!")
    else:
        print("valores válidos!")
        break
        
produto=x*y #Valor de N
relativo=(x-1)*(y-1) #Função totiente de N = φ(x)
divisores_de_relativo = divisor(relativo)  
while True:
    while True:
        e = int(input(f'Insira um valor entre 1 e {relativo}, que seja relativamente primo a {relativo}: '))
        divisores_de_e = divisor(e)
        eh_coprimo = coprimo(divisores_de_e, divisores_de_relativo)
        if eh_coprimo == 0:
            break
    result=euclides(relativo,e)
    if(result == 1):
        print("sua chave foi gerada!")
        print("voce pode encontra-la no arquivo key.txt gerado na pasta atual")
        break

with open("key.txt", "w") as f:
    f.write(str(produto)+"\n")
    f.write(str(e)+"\n")