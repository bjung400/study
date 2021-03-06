#include <stdio.h>
int arr[10001] = {0, };
int check;
int d(int n)
{
    int sum = n;
    while(1)
    {
        if (n == 0) return sum;
        sum += n % 10;
        n = n / 10;
    }
}

int main()
{
    for (int i = 1; i <= 10001; i++)
    {
        check = d(i);
        if (check < 10001)
        {
            arr[check] = 1;
        }
    }
    for (int i =1; i <= 10001; i++)
    {
        if (arr[i] == 0) printf("%d\n", i);
    }
}