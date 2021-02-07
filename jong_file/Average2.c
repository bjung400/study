#include <stdio.h>

float average(int length, int array[]);

int main(void)
{
	int n;
	
	printf("Score : ");
	scanf("%d", &n);

	int score[n];
	for (int i = 0; i < n; i++)
	{
		printf("Score %i : ", i + 1);
		scanf("%i", &score[i]);
	}

	printf("Average : %.1f\n", average(n, score));
}

float average(int length, int array[])
{
	int sum = 0;
	for (int i = 0; i < length; i++)
	{
		sum += array[i];
		printf("%i sum : %i \n", i + 1, sum);
	}
	
	return (float) sum / (float) length;
}
