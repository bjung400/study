#include <stdio.h>
#include <string.h>
int main(void)
{
    int size, n, sum;
    char ox[81];
    scanf ("%d", &size);

    for (int i = 0; i < size; i++)
    {
        n = 1, sum = 0;
        scanf ("%s", ox);

        for (int j = 0; j < strlen(ox); j++)
        {
            if (ox[j] == 'O') sum += n, n++;
            else n = 1;
        }
        //printf("%d\n", (int)strlen(ox));
        printf("%d\n", sum);
    }
}