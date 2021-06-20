#include <stdio.h>

int main(void)
{
	int H, M;
	
	scanf("%d %d", &H, &M);

	if (0 <= H && 23 >= H && 0 <= M && 59 >= M)
	{
		M = M - 45;
		if (M < 0)
		{
			H = H - 1;
			M = M + 60;
		}
		if (H < 0)
		{	
			H = H + 24;
		}
		printf("%d %d\n", H, M);
	}
	return 0;
}
