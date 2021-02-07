#include <stdio.h>
void self_service(void);

int main (void)
{
	self_service();
	return 0;
}

void self_service(void)
{
	int i=1;   // 조건문을 위해  int 선언

	if(i>5)
		return;

	printf("셀프 서비스 %d회 \n", i);
	i=i+1           //i에 1추가후 함수를 다시호출
	self_service();
}

