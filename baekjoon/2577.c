#include <stdio.h>
#include <string.h>
int main(void)
{
    int A, B, C, sum;
    char str[100];
    int n[10] = {0, };

    scanf("%d %d %d", &A, &B, &C);
    sum = A * B * C;
    sprintf(str, "%d", sum);
    for (int i = 0; i < strlen(str); i++)
    {
        n[str[i] - '0']++;
    }
    for (int i = 0; i < 10; i++){printf("%d\n", n[i]);}
}