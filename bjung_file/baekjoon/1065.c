// #include <stdio.h>

// int hansu(int N, int size);
// int N_div(int arr[]);

// int arr[1001] = {0};
// int count = 0;

// int main()
// {
//     int N, temp;
    
//     scanf("%d", &N);
//     temp = N;
// }
// int hansu(int N, int size)
// {
    
//     if (N <= 99)
//     {
//         count = N;
//         return count;
//     }
//     else
//     {
//         for (int i = 100; i <= N; i++)
//         {
//             arr[i] = i;       
//         }
//     }
//     N_div(arr);
// }
// int N_div(int arr[])
// {
//     int temp_arr[sizeof(arr) / sizeof(int)];
//     int temp;
//     for (int i = 100; i <= arr; i++)
//     {
//         for (int j = 1; j <= 10; j++)
//         {
            
//         }
//     }  
    
// }
#include <stdio.h>

int main(void)
{
    int N, temp100 = 0, temp10 = 0, temp1 = 0, count = 0;
    int arr[1001];
    
    scanf("%d", &N);
    if (N <= 99)
    {
        printf("%d", N);
        return 0;
    }
    else
    {
        count += 99;
        
        for (int i = 100; i <= N; i ++)
        {
            temp100 = i / 100;
            temp10 = (i % 100) / 10;
            temp1 = i % 10;
            if(temp100 - temp10 == temp10 - temp1)
            {
                count++;
            }
        }
    }
    printf("%d", count);
}