#include <stdio.h>

int main(void)
{
	int N;

	scanf("%d", &N);

	if(1 <= N && 100 >= N)
	{
		for(int i = 1; i <= N; i++)
		{
			for(int n = 0; i > n; n++)
			{
				printf("*");
			}
			printf("\n");
		}
	}
	
	return 0;
}
