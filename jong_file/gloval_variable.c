#include <stdio.h>
int num;  //전역 변수 int 선언
void grow(void);

int main(void)
{
	printf("함수 호출전 num : %d \n", num);

	grow();
	printf("함수 호출후  num :%d \n", num);

	return 0;
}

void grow (void)
{
	num=60;  // 전역변수 num 값 변경
}


