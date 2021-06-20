#include <stdio.h>

int main(void)
{
    int N, N1, N2, count = 0, original = 0, sum = 0;
    scanf("%d", &N);
    original = N;
    if(N >= 0 && N <= 99)
    {
        do{
            N1 = N / 10;
            N2 = N % 10;
            sum = N1 + N2;
            if(sum > 9)
            {
                sum = sum % 10;
            }
            N = (N2 * 10) + (sum);
            count++;
        }while(original != N);
        printf("%d", count);
    }
    return 0;
}