#include <stdio.h>

int inversoMod(int a, int b, int c)
{
    if (b < c)
    {
        if (a * b % c == 1)
        {
            return b;
        }
        else
        {
            inversoMod(a, ++b, c);
        }
    }
    else
    {
        return 0;
    }
}

int main()
{
    int a, c;
    int b = 0;
    int res = 0;

    printf("Calculadora de mod em C.\n\n");
    printf("Digite o valor do dividendo: ");
    scanf("%d", &a);
    printf("Agora digite o valor do divisor: ");
    scanf("%d", &c);

    res = inversoMod(a, b, c);

    if (res != 0)
    {
        printf("Inverso modular de %d mod %d eh: %d", a, c, res);
    }
    else
    {
        printf("Nao existe inverso modular para este numero inteiro.\n");
    }
    
    return 0;
}