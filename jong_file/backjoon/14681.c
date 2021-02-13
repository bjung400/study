#include <stdio.h>
int main()
{
	int x, y;
	scanf("%d %d", &x, &y); //x,y 입력받고 사분면출력하기
	if (x > 0 && y > 0)
	 	printf("1\n");
	else if (x < 0 && y > 0)
		printf("2\n");
	else if (x < 0 && y < 0)
		printf("3\n");
	else if (x > 0 && y < 0)
		printf("4\n");
	return 0;
}

