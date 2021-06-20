#include <stdio.h>

int main(void)
{
    int A, B, C, sum;
    int n[10] = {0, };
    
    scanf("%d %d %d", &A, &B, &C);
    sum = A * B * C;
    while (0 < sum)
    {
        n[sum % 10]++;
        sum /= 10;
    }
    for (int i = 0; i < 10; i++) 
    {
        printf("%d\n", n[i]);
    }
    return 0;
}