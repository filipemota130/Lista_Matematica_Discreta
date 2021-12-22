#include <stdio.h>

// Sistema de Congruência

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
    else
        return D;
}

int congruencia(int a, int b, int m, int i)
{
    if (a == 1)
    {
        return b;
    }

    if (i < m)
    {
        if ((i * a) % m == b)
        {
            return i;
        }
        congruencia(a, b, m, ++i);
    }
    else
        return 0;
}

int main()
{
    printf("Programa que encontra a solucao unica sistemas com tres congruencias lineares:\n\n");

    int a1, b1, m1, a2, b2, m2, a3, b3, m3;

    printf("Digite o valor de A da primeira congruencia: ");
    scanf("%d", &a1);
    printf("Digite o valor de B da primeira congruencia: ");
    scanf("%d", &b1);
    printf("Digite o valor de M da primeira congruencia: ");
    scanf("%d", &m1);

    printf("\nDigite o valor de A da segunda congruencia: ");
    scanf("%d", &a2);
    printf("Digite o valor de B da segunda congruencia: ");
    scanf("%d", &b2);
    printf("Digite o valor de M da segunda congruencia: ");
    scanf("%d", &m2);

    printf("\nDigite o valor de A da terceira congruencia: ");
    scanf("%d", &a3);
    printf("Digite o valor de B da terceira congruencia: ");
    scanf("%d", &b3);
    printf("Digite o valor de M da terceira congruencia: ");
    scanf("%d", &m3);

    if (mdc(a1, m1) == 1 && mdc(a2, m2) == 1 && mdc(a3, m3) == 1 && mdc(m1, m2) == 1 && mdc(m1, m3) == 1 && mdc(m2, m3) == 1)
    {
        int B1 = congruencia(a1, b1, m1, 1);
        int B2 = congruencia(a2, b2, m2, 1);
        int B3 = congruencia(a3, b3, m3, 1);

        int n1 = m2 * m3;
        int n2 = m1 * m3;
        int n3 = m1 * m2;

        int aux1 = n1 % m1;
        int aux2 = n2 % m2;
        int aux3 = n3 % m3;

        int s1 = congruencia(aux1, 1, m1, 1);
        int s2 = congruencia(aux2, 1, m2, 1);
        int s3 = congruencia(aux3, 1, m3, 1);

        int s = ((B1 * n1 * s1) + (B2 * n2 * s2) + (B3 * n3 * s3)) % (m1 * m2 * m3);

        printf("\nA solucao unica desse sistema de congruencias lineares eh: %d\n", s);
    }
    else
    {
        printf("\nComo os valores nao sao coprimos, nao temos como descobrir o resultado do sistema por esse metodo.\n");
    }

    return 0;
}