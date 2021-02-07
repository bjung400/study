#include <stdio.h>

void main ()
{
	int i1, i2, sum, sub;
	printf("두 정수를 입력");
	scanf("%d %d", &i1, &i2);
	sum = i1 + i2;
	sub = i1 - i2;
	printf(" 합 : %d + %d = %d \n", i1, i2, sum);	
	printf(" 차 : %d - %d = %d \n", i1, i2, sub);
	
	return;
}
	
