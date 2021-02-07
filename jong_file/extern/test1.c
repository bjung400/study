#include <stdio.h>

int main(void)
{	
	extern int num1;  
	extern int num2;  
	extern int num3;

	printf("num1의 값 :%d \n", num1);
	printf("num1의 값 :%d \n", num2);
	printf("num1의 값 :%d \n", num3);
	printf("덧셈 결과 : %d \n", num1+num2+num3);
	return 0;
}
