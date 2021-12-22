a = int(input("primeiro inteiro: "))
b = int(input("segundo inteiro: "))
# swap
if(b > a):
    aux = b
    b = a
    a = aux
resto = [a, b]
quociente = [0, 0]


def euclides(a, b):
    while b != 0:
        result = a % b
        resto.append(result)
        quociente.append(a//b)
        a = b
        b = result
    return a


valor_s = [1, 0, ]
valor_t = [0, 1, ]

mdc = euclides(a, b)
print(mdc)
if (mdc == b):
    valor_s.append(valor_s[0] - (valor_s[1]*quociente[2]))
    valor_t.append(valor_t[0] - (valor_t[1]*quociente[2]))
    print("a*s + b*t = mdc(a,b) ==> ", str(a)+"*s +", str(b)+"*t =", mdc)
    print("valor de s =", 0, "valor de t =", 1)
else:
    print(resto, quociente)
    for i in range(len(resto)):
        valor_s.append(valor_s[i] - (valor_s[i+1]*quociente[i+2]))
        valor_t.append(valor_t[i] - (valor_t[i+1]*quociente[i+2]))
        if(resto[i+2] == mdc):
            print("a*s + b*t = mdc(a,b) ==> ",
                  str(a)+"*s +", str(b)+"*t =", mdc)
            print("valor de s =", valor_s[i+2], "valor de t =", valor_t[i+2])
            break
    print(valor_s, valor_t)
