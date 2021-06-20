#include <stdio.h>

int main(void)
{
    int C, C2;
    int sum, count;
    int arr[1001];
    scanf ("%d", &C);
    for (int i = 0; i < C; i++)
    {
        scanf("%d", &C2);
        sum = 0, count = 0;
        for (int j = 0; j < C2; j++)
        {
            scanf("%d", &arr[j]);
            sum += arr[j];
        } 
        for (int k = 0; k < C2; k++)
        {
            if ((sum / C2) < arr[k])
            {
                count++;
            }
        }
        printf("%.3f%%\n", ((float)count / (float)C2) * 100);
    }
}