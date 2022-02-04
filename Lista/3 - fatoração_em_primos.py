print("=== Calculadora de fatoração ===")
n = int(input("insira o numero a ser fatorado: "))
aux = n
potencia = 0
fator = 2
while n != 1:
    if(n % fator == 0):
        n = n//fator
        potencia += 1
    else:
        if(potencia != 0):
            print(str(fator)+"^"+str(potencia), end='  X  ')
            potencia = 0
        fator += 1
if(potencia != 0):
    print(str(fator)+"^"+str(potencia), "=", aux)
