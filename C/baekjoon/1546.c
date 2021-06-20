#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    float n, max = 0, sum = 0;

    scanf("%f", &n);
    float *nptr = malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++)
    {
        scanf("%f", &nptr[i]);
        if(max < nptr[i])
        {
            max = nptr[i];
        }
        sum += nptr[i];
    }
    printf("%f", ((sum / max) * 100) / n);
    free(nptr);
    return 0;  
}