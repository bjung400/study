#include <stdio.h>
int sum();
int input();
void output(int x);

int main()
{
	int result;
	printf("---프로그램 시작---\n");
	printf("정수 한개를 입력하세요 : ");

	result=sum();
	output(result);

	return 0;
}

int sum()
{
	int total=0, num=0;
	num=input();

	for(int i=1; i<=num; i++)
	{
		total=total+i;
	}
	return total;
}

int input()
{
	int val;
	scanf("%d", &val);
	return val;
}

void output(int x)
{
	printf("결과 : %d \n", x);
	return;
}

