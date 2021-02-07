#include <stdio.h>
#include <math.h>

int main(void)
{
	int num1, num2;
	double num3;
	scanf("%d %d", &num1, &num2); 
	num3 = num2;
	printf("%d\n", num1 * (num2 % 10));
	printf("%d\n", num1 * ((num2 / 10) % 10));
	printf("%d\n", num1 * (num2 / 100));
	printf("%d\n", num1 * num2); 
	num3 = (num3 / 10) ;
	printf("%f\n", fmodf(num3, 10));
	return 0;
}

