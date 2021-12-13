n = 12000000
contador = 0
lista = []
for i in range(n+1):
    lista.append(True)
for multiplo in range(2, int(len(lista)/2)):
    for n in range(2*multiplo, len(lista), multiplo):
        if (lista[n] == True):
            lista[n] = False
for j in range(len(lista)):
    if (j >= 2 and lista[j] == True):
        contador += 1
        print(j)
print("numero de primos:", contador)
