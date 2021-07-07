#include <stdio.h>
int foo(int year)
{
	if((year % 4 != 0 || year % 100 == 0) && year % 400 != 1)
	{
		printf("평년");
	}
	else
	{
		printf("윤년");
	}
	return 0;
}
int main()
{
	foo(1900);
}
