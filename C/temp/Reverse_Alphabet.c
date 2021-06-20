#include <string.h>
#include <stdio.h>

int main(void)
{
    char s[100];
    printf("Input Alphabet : ");
    scanf("%s", s); // %c로하면 공백은 입력되지않음 
    printf("Reverse Alphabet : ");
    for(int i = 0, n = strlen(s); i < n; i++)
    {
        if(s[i] >= 'A' && s[i] <= 'Z')
        {
            printf("%c", s[i] + 32);
        }
        else if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32);
        }
	else
	{
		printf("%c", s[i]);
	}
    }
    printf("\n");
}
