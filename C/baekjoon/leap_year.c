#include <stdio.h>

int main(void)
{
	int nbr = 0;
	
	scanf("%d", &nbr);
	
	if ( nbr >= 1 && nbr <= 4000 && nbr % 4 == 0)
		if ( nbr % 100 != 0 || nbr % 400 == 0) 
			printf("1\n");
		else
			printf("0\n");
	else
		printf("0\n");
	return 0;
}

