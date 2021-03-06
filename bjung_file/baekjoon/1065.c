#include <stdio.h>

int hansu(int N, int size);
int N_div(int arr[]);

int arr[1001] = {0};
int count = 0;

int main()
{
    int N, temp;
    
    scanf("%d", &N);
    temp = N;
}
int hansu(int N, int size)
{
    
    if (N <= 99)
    {
        count = N;
        return count;
    }
    else
    {
        for (int i = 100; i <= N; i++)
        {
            arr[i] = i;       
        }
    }
    N_div(arr);
}
int N_div(int arr[])
{
    int temp_arr[sizeof(arr) / sizeof(int)];
    int temp;
    for (int i = 100; i <= arr; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            
        }
    }  
    
}