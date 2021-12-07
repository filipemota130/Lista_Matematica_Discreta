import time
import math
x = 17
y = 13


def Primo(n, i):
    while (i < n):
        if (n % i == 0):
            return 0
        else:
            i = i + 1
    return n


tempo_ini = time.time()
while time.time() - tempo_ini < 60:
    result = Primo(x, 2)
    if(result != 0):
        print(x)
    x += 1
