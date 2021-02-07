#include <stdio.h>

int main(void)
{
	int score;
	
	scanf ("%d", &score);

	if (score > 89 && score < 101)
		printf("A\n");
	else if (score > 79 && score < 90)
		printf("B\n");
	else if (score > 69 && score < 80)
		printf("C\n");
	else if (score > 59 && score < 70)
		printf("D\n");
	else
		printf("F\n");

	return 0;
}
