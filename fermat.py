import time
import random


def mdc(n1, n2):
    result = n1 % n2
    if (result != 0):
        return mdc(n2, result)
    else:
        return n2


def Primo(x, y):
    p = mdc(x, y)
    if(p == 1):
        if(((y**(x-1)) % x) == 1):
            return 1
        else:
            return 0
    else:
        return 0


n = 3
contador = 0

tempo_ini = time.time()
while time.time() - tempo_ini < 60:
    aleatorio = random.randint(2, n-1)
    result = Primo(n, aleatorio)
    if(result != 0):
        maior = n
        contador += 1
        print(maior)
    n += 1
print("numero total de primos encontrados:", contador)
