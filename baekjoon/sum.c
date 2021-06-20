#include <stdio.h>

int main(void)
{
	int n, sum = 0;

	scanf("%d", &n);
	if (1 <= n && 10000 >= 1)
	{	
		for(int i = 1; i <= n; i++)
		{
			sum += i;
		}
	}
	printf("%d\n", sum);
	return 0;
}

