n = int(input())
aux = n
potencia = 0
fator = 2
while n != 1:
    if(n % fator == 0):
        n = n//fator
        potencia += 1
    else:
        if(potencia != 0):
            print(fator, "^", potencia, end='  X  ')
            potencia = 0
        fator += 1
if(potencia != 0):
    print(fator, "^", potencia, "=", aux)
