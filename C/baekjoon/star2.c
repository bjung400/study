#include <stdio.h>

int main(void)
{
	int N, x;

	scanf("%d", &N);
	x = N;

	if(1 <= N && 100 >= N)
	{
		for(int i = 1; i <= N; i++)
		{
			for(int n = 0; i > n; n++)
			{
				for(int t = 1; t < x; x--)
				{
					printf(" ");
				}
				printf("*");
			}
			printf("\n");
			x = N - i;
		}
	}
	
	return 0;
}
