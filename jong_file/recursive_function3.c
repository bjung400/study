#include <stdio.h>
void self_service(int n);

int main (void)
{
	int a=1;
	self_service(a);       // 셀프 서비스 함수에 변수 a값을  전달하며 함수호출
	return 0;
}

void self_service(int n)    //매개변수n = a ,  a의값이 매개변수 n에 저장됨
{
	if(n>5)
		return;

	printf("..셀프 서비스 %d회 \n", n);
	self_service(n+1);
}
