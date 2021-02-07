#include <stdio.h>
double divide(double x, double y);
double input(void);
void output(double x);
void information();

	
int main()
{
	double num1, num2, result;

	information();
	printf("첫 번재 실수 입력 : ");
	num1 = input();

	printf("두 번째 실수 입력 : ");
	num2=input();
	
	result=divide(num1, num2);
	output(result);
	return 0;
}

double divide(double x, double y)
{
	double val;
	val=x/y;
	return val;
}
double input()
{
	double val;
	scanf("%lf", &val);
	return val;
}
void output (double x)
{
	printf("나눗셈22 결과 : %lf \n" ,x);
	return;
}
void information()
{
	printf("---프로그램 시작---\n");
	return;
}	

