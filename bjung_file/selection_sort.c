#include <stdio.h>

int print_arr(int *ptr, int size);
int arr[8] = {6, 3, 8, 5, 2, 7, 4, 1};
int size = sizeof(arr) / sizeof(int);
int main(void)
{
    int temp;
    int n;
    int count = 0;
    int j = 0;
    printf("정렬전\n");
    print_arr(arr, size);
    printf("\n");
    
    for(int i = 0; i < sizeof(arr) / sizeof(int) - 1; i++)
    {
        for(int j = i + 1; j < sizeof(arr) / sizeof(int); j++)
        {
            count += 1;
            if(arr[i] > arr[j])
            {
                temp = arr[i];
                printf("(%d) swap ",arr[i]);
                arr[i] = arr[j];
                printf("(%d) \n", arr[j]);
                arr[j] = temp;
                print_arr(arr, size);
            }
        }
    }
    printf("\n정렬후\n");
    for(int i = 0; i < sizeof(arr) / sizeof(int); i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n%d\n",count);
}

int print_arr(int *ptr, int size)
{
    for(int i = 0; i < size; i++)
    {
        printf("%d ",ptr[i]);
    }
    printf("\n");
    return 0;
}