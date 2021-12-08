import time
x = 3
maior = 0
contador = 0


def Primo(n, i):
    while (i < n):
        if(i >= n**0.5):
            return n
        if (n % i == 0):
            return 0
        else:
            i = i + 1
    return n


tempo_ini = time.time()
while time.time() - tempo_ini < 60:
    result = Primo(x, 2)
    if(result != 0):
        maior = x
        contador += 1
        print(maior)
    x += 1
print("numero total de primos encontrados:", contador)
