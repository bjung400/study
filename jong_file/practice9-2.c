#include <stdio.h>
int sum(int x);

int main (void)
{
 	int i;

	for(i=1; i<=12; i++)
	{
		printf("%d", sum(i));
	}

	printf("\n");
}

int sum (int x)
{
	if (x <= 2)
		return 1;   //매개변수가 2일때까지 1을 반환하는 리턴문
	else 
		return sum(x-1) + sum(x-2);      //리턴문을 이용한 재귀함수
}
