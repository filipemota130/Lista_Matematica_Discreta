import math
print("\nCalculadora de mdc e mmc entre dois números")
n = int(input("\ninsira o primeiro valor: "))
p = int(input("insira o segundo valor: "))
aux1 = n
aux2 = p
array_n = [1, ]
array_p = [1, ]
mdc = []
mmc = []


def lista_para_mdc(n, fator, array):
    while n != 1:
        if(n % fator == 0):
            n = n//fator
            if not fator in array:
                array.append(fator)
        else:
            fator += 1

    # mdc
lista_para_mdc(n, 2, array_n)
lista_para_mdc(p, 2, array_p)

for j in range(len(array_n)):
    if(array_n[j] in array_p):
        mdc.append(array_n[j])

# mmc
array_n = [1, ]
array_p = [1, ]
array_exponent = [1, ]
array_exponent2 = [1, ]


def lista_para_mmc(n, fator, array, potencia):
    while n != 1:
        if(n % fator == 0):
            n = n//fator
            potencia += 1
            if(n == 1):
                if not fator in array:
                    array.append(fator**potencia)
            array_n.append(fator)
        else:
            if not fator**potencia in array:
                array.append(fator**potencia)
            potencia = 0
            fator += 1


lista_para_mmc(n, 2, array_exponent, 0)
lista_para_mmc(p, 2, array_exponent2, 0)


def build_mmc(array_exponent, array_exponent2, mmc):
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


build_mmc(array_exponent, array_exponent2, mmc)
print("\nresultados:")
print("mdc(%d,%d) =" % (aux1, aux2), math.prod(mdc))
print("mmc(%d,%d) =" % (aux1, aux2), math.prod(mmc))
