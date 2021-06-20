#include <stdio.h>

int main(void)
{
	int x, y;

	scanf("%d %d", &x, &y);

	if (-1000 <= x && 1000 >= x && x != 0 && -1000 <= y && 1000 >= y && y != 0) 
		if (x >= 1 && y >= 1)
			printf("1\n");

		if (x <= -1 && y >= 1)
			printf("2\n");

		if (x <= -1 && y <= -1)
			printf("3\n");

		if (x >= 1 && y <= -1)
			printf("4\n");

	return 0;
}
