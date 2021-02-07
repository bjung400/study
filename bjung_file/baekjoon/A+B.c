#include <stdio.h>

int main(void)
{
	int T, A, B;

	scanf("%d", &T);

	if(T <= 1000000)
	{
		for(int i = 0; T > i; i++)
		{
			scanf("%d %d", &A, &B);
			printf("%d\n", A+B);
		}
	}
	
	return 0;
}
