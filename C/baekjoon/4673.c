#include <stdio.h>
#define MAX_NUM 10001

int selfnumber(int n)
{
    int sum = n;
    while (1)
    {
        if (n == 0) return sum;
        sum += n % 10;
        n /= 10;
    }
}
    int main(void)
    {
    int arr[MAX_NUM], i, check;

    for (i = 1; i < MAX_NUM; i++)
    {
        check = selfnumber(i);
        if (check < MAX_NUM)
            arr[check] = 1;
    }
    for (i = 1; i < MAX_NUM; i++)
    {
        if (arr[i] != 1)
            printf ("%d\n", i);
    }
    return 0;
}