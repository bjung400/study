#include <stdio.h>

int main(void)
{
    int A, B, result = 0;
    int n[10] = {0, };

    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &n[i]);
        n[i] = n[i] % 42;
    }
    for (int i = 0; i < 10; i++)
    {
        int C = 0;
        for (int j = 0; j < i; j++)
        {
            if (n[i] == n[j])
                C++;
        }
        if (C == 0)
        {
            result++;
        }
    }
    printf("%d\n", result);
}