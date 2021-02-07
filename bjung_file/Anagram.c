#include <stdio.h>

void bubble_sort(int arr[], int length);
void swap(int *a, int *b);
//사용자정의함수를 사용해서 코드의 길이를 줄였고 간결하게 작성했고
//버블정렬로 정렬한뒤 두배열의 인덱스를 비교하여 틀리면  False 출력후 종료하였고 모두 맞으면 True를 출력후 종료했습니다
int main(void)
{
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[5] = {1, 2, 3, 4, 5};
    int size = sizeof(arr1) / sizeof(int);

    bubble_sort(arr1, size);
    bubble_sort(arr2, size);
    
    for (int i = 0; i < size; i++)
    {
        if (arr1[i] != arr2[i])
        {
            printf("False\n");
            return 0;
        }
    }

    printf("True\n");
    return 0;
}

void bubble_sort(int arr[], int length)
{
    for (int i = 0; i < length - 1; i++)
    {
        for (int j = 0; j < length - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}