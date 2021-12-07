import time
import math
x = 7940627
maior = 0


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
while time.time() - tempo_ini < 120:
    result = Primo(x, 2)
    if(result != 0):
        maior = x
    x += 1
print(maior)
# teste de alteração na branch
