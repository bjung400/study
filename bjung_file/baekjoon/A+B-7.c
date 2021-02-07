#include <stdio.h>

int main(void)
{
	int T, A, B;

	scanf("%d", &T);

	for(int i = 1; T >= i; i++)
	{
		scanf("%d %d", &A, &B);
		if(A > 0 && B < 10)
		{
			printf("Case #%d: %d\n", i, A + B);
		}
	}
	return 0;
}	
