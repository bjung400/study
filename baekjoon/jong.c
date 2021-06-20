#include <stdio.h>
int main(void)
{
	int n;

	//scanf("%d", &n);
    n = 5;
	for (int i = 0; i < n; i++) //상위 for문
	{
		printf("          j는 0으로 초기화\n");
		for (int j = 0; j <= i; j++) //중첩 for문
		{
			printf("*");
		}
        printf("          중첩for문 종료");
		printf("\n");
	}
	printf("          상위for문 종료");
	return 0;
}