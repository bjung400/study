#include <stdio.h>

int main(void)
{
	int N;

	scanf("%d", &N);

	if(N <= 100000)
	{
		for(int i = 0; i < N; N--)
		{
			printf("%d\n", N);
		}
	}

	return 0;
}
