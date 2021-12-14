import math

n = int(input())
p = int(input())
aux1 = n
aux2 = p
array_n = [1, ]
array_p = [1, ]
mdc = []
mmc = []

# mdc
fator = 2
while n != 1:
    if(n % fator == 0):
        n = n//fator
        if not fator in array_n:
            array_n.append(fator)
    else:
        fator += 1

fator = 2
while p != 1:
    if(p % fator == 0):
        p = p//fator
        if not fator in array_p:
            array_p.append(fator)
    else:
        fator += 1

for j in range(len(array_n)):
    if(array_n[j] in array_p):
        mdc.append(array_n[j])
# mmc
n = aux1
p = aux2
array_n = [1, ]
array_p = [1, ]
array_exponent = [1, ]
array_exponent2 = [1, ]
potencia = 0
fator = 2
i = 1
while n != 1:
    if(n % fator == 0):
        n = n//fator
        potencia += 1
        if(n == 1):
            if not fator in array_exponent:
                array_exponent.append(fator**potencia)
        array_n.append(fator)
    else:
        if not fator**potencia in array_exponent:
            array_exponent.append(fator**potencia)
        potencia = 0
        i += 1
        fator += 1


potencia = 0
i = 1
fator = 2
while p != 1:
    if(p % fator == 0):
        p = p//fator
        potencia += 1
        if(p == 1):
            if not fator in array_exponent2:
                array_exponent2.append(fator**potencia)
        array_p.append(fator)
    else:
        if not fator**potencia in array_exponent2:
            array_exponent2.append(fator**potencia)
        potencia = 0
        i += 1
        fator += 1

for n in range(len(array_exponent)):
    for i in range(len(array_exponent2)):
        if (int(array_exponent[n]) % int(array_exponent2[i]) != 0):
            if not array_exponent2[i] in mmc:
                mmc.append(array_exponent2[i])
        if (int(array_exponent2[i]) % int(array_exponent[n]) != 0):
            if not array_exponent[n] in mmc:
                mmc.append(array_exponent[n])

mmc.sort()
contador = 0
j = 1
while contador < len(mmc):
    divisor = False
    while j < len(mmc):
        if(mmc[j] % mmc[contador] == 0):
            del mmc[contador]
            divisor = True
            break
        j += 1
    if(divisor == False):
        contador += 1

print("mdc(%d,%d) =" % (aux1, aux2), math.prod(mdc))
print("mmc(%d,%d) =" % (aux1, aux2), math.prod(mmc))
