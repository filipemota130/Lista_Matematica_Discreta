#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int Primo(int n, int i)
{
    if (i >= n / 2)
    {
        return 1;
    }
    else
    {
        if (n % i == 0)
        {
            return 0;
        }
        else
        {
            i = i + 1;
            Primo(n, i);
        }
    }
}

int main()
{
    int num;
    int i = 2;
    scanf("%i", &num);
    if (num < 2)
    {
        printf("não é primo\n");
        return 0;
    }
    int retorno = Primo(num, i);
    if (retorno == 0)
    {
        printf("não é primo\n", retorno);
    }
    else
    {
        printf("é primo\n", retorno);
    }
    return 0;
}