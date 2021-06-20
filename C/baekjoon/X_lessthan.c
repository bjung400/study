#include <stdio.h>

int main(void)
{
    int A[10000], N, X;

    scanf("%d %d", &N, &X);
    
    if(1<=N && X <= 10000)
    {
        for(int i = 0; i < N; i++)
        {
            scanf("%d", &A[i]);
        }
        for(int i = 0; i < N; i++)
		{
            if(A[i] < X)
            {
                printf("%d ", A[i]);
            }
        }
    }
    return 0;
}