#include <stdio.h>
#define MAX 10001

int no_selfnum (int n);
int arr[MAX] = {0, }, sum, check;

int main(void)
{
    for (int i = 1; i < MAX; i++)
    {
        check = no_selfnum(i);
        if (check < MAX)
        {
            arr[check] = 1;
        }
    }
    for (int i = 1; i < MAX; i++)
    {
        if (arr[i] == 0) printf("%d\n", i);
    }
}
int no_selfnum (int n)
{
    sum = n;
    while (1)
    {
        if (n == 0) return sum;
        sum += n % 10;
        n /= 10;
    }
}
