#include <stdio.h>

// Congruencia Linear

int mdc(int A, int D)
{
    if (A < D)
    {
        int aux;
        aux = A;
        A = D;
        D = aux;
    }
    int resto = A % D;
    if (resto != 0)
    {
        A = D;
        D = resto;
        mdc(A, D);
    }
    else return D;
}

int congruencia(int a, int b, int m, int i, int M, int solucoes)
{
    if (i < M)
    {
        if ((i * a) % m == b)
        {
            printf("Uma das solucoes eh: %d\n", i);
            solucoes++;
        }
        congruencia(a, b, m, ++i, M, solucoes);
    }
    else
    {
        if ((i * a) % m == b)
        {
            printf("Uma das solucoes eh: %d\n", i);
            solucoes++;
        }

        if (solucoes == 0)
        {
            printf("Essa congruencia nao possui nenhuma solucao.\n");
        }

        return 0;
    }
}

int main()
{
    int a, b, m;

    printf("Programa para encontrar solucoes inteiras (entre 0 e m) de ax = b (mod m).\n\n");
    printf("Digite o valor de A: ");
    scanf("%d", &a);
    printf("Digite o valor de B: ");
    scanf("%d", &b);
    printf("Digite o valor de M: ");
    scanf("%d", &m);

    printf("\nCongruencia linear de: %dx = %d (mod %d)", a, b, m);

    int d = mdc(a, m);

    printf("\nTirando o mdc de A e M, temos o valor D = %d, que eh o numero de solucoes dessa congruencia.\n\n", d);

    if (d == 1)
    {
        congruencia(a, b, m, 1, m, 0);
    }
    else
    {
        congruencia(a/d, b/d, m/d, 1, m, 0);
    }

    return 0;
}