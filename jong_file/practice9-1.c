#include <stdio.h>
int a, result;
int abs(int n);

int main (void)
{
	printf("정수를 입력하세요^^ : ");
	scanf("%d", &a);
	result=abs(a);
	printf("절대값은 : %d 입니다", result);
}

int abs(int n)
{
	if (n>=0)
		return n;
	else 
		return -n;
}
