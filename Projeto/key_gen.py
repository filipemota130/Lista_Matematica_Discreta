def euclides(A,D):
    resto = 1
    while resto>0:
        resto = A % D
        A = D
        D = resto
    return A

def eh_primo(n, i):
    if (i >= n/2):
        return 1
    else:
        if (n % i == 0):
            return 0
        else:
            i = i + 1
            eh_primo(n, i)
i=0
while i==0:
    x=int(input("#1 insira um numero primo: "))
    y=int(input("#2 insira um numero primo: "))
    verifica=eh_primo(x,2)
    verifica2=eh_primo(y,2)
    if(x<2 or y<2 or verifica==0 or verifica2==0):
        print("valores inválidos, não são primos!")
    else:
        print("valores válidos!")
        i=1
        
produto=x*y
relativo=(x-1)*(y-1)
    
i=0
while i==0:
    print("insira um valor relativamente primo a",relativo)
    e=int(input())
    result=euclides(relativo,e)
    if(result == 1):
        print("sua chave foi gerada!")
        print("voce pode encontra-la no arquivo key.txt gerado na pasta atual")
        i=1
        
with open("key.txt", "w") as f:
    f.write(str(produto)+"\n")
    f.write(str(e)+"\n")