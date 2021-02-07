#include <stdio.h>

int main(void)
{
    int arr[8] = {6, 3, 8, 5, 2, 7, 4, 1};
    int temp;
    int count = 0;
    printf("정렬전\n");
    for(int i = 0; i < sizeof(arr) / sizeof(int); i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
    for(int i = 0; i < sizeof(arr) / sizeof(int) - 1; i++)
    {
        for(int j = 0; j < sizeof(arr) / sizeof(int) - 1; j++)
        {
            count += 1;
            if(arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
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
