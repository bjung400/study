#include <stdio.h>
int main()
{
	int h, m;
	scanf("%d %d", &h, &m);
	if (h > 0  && m >= 45)
		printf("%d %d", h, m-45);
	else if (h > 0 && m < 45)
		printf("%d %d", h-1, 60+m-45);
	else if (h == 0 && m >= 45)
		printf("%d %d", 0, m-45);
	else if (h == 0 && m < 45)
		printf("%d %d", 24-1 , 60+ m-45);
	return 0;
}
