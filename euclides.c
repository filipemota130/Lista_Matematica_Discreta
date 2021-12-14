    #include <stdio.h>

    int euclides(int A, int D)
    {
        int resto;      // Criando variável de resto.

        resto = A % D;  // Atribuindo o valor de resto.

        if (resto != 0)     // Cálculo feito baseado na tabela do algoritmo de Euclides.
        {
            A = D;
            D = resto;
            euclides(A, D);
        }
        else
        {
            return D;
        }
    }

    void contagem(int n)
    {
        int A, D, res;      // Criando variáveis do cálculo do MDC.

        if(n > 0)           // Checando se a contagem ainda está rolando.
        {
            printf("Digite os dois valores para tirar o MDC: ");
            scanf("%d %d", &A, &D);     // Scaneia A e D.

            if (A < D)      // Inverter valores de A e D para o cálculo, pois A deve ser maior que D.
            {
                int aux;
                aux = A;
                A = D;
                D = aux;
            }

            printf("MDC(%d,%d) = ", A, D);  // Printando a apresentação do cálculo.

            res = euclides(A, D);       // Atribuindo o valor do MDC calculado na função a variável Resultado.

            printf("%d\n", res);        // Printando o resultado do cálculo.

            contagem(n - 1);
        }
    }

    int main()
    {
        int n;      // Criando variável N.

        printf("Calculadora de MDC baseada em Euclides.\n\n");

        //printf("Digite o numero de operacoes que deseja fazer e os dois valores de cada.\n\n");

        printf("Digite o numero de operacoes que deseja fazer: ");
        scanf("%d", &n);    // Receber o número de operações a serem feitas.

        contagem(n);        // Chamando a função de contagem e cálculo.

        return 0;
    }