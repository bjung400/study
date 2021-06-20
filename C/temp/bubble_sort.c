#include <stdio.h>

void swap(int arr[], int count);

int main(void)
{
	int array[10] = {7, 8, 9, 5, 4, 3, 2, 1, 6};	
	swap(array, sizeof(array) / sizeof(int));
	for(int i = 0; i < 10; i++)
	{
		printf("%d\n",array[i]);
	}
	printf("%ld", sizeof(array) / sizeof(int));
	return 0;
}

void swap(int arr[], int c)
{
	int tmp = 0;

        for (int i = 0; i < c; i++)
        {
		printf("\n%d번째 사이클\n\n", i); 
                for(int j = 0; j < c - 1; j++)
                {
			printf("%d번째 비교\n", j);
                        if (arr[j] > arr[j+1])
                        {
                                tmp = arr[j];
                                arr[j] = arr[j+1];
                                arr[j+1] = tmp;
				printf("%d와 %d교환\n", arr[j], arr[j+1]);
                        }
                }
        }
}
