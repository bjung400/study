#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char s[50];
    printf("Input Alphabet : ");
    scanf("%[^\n]", s); // %c로하면 공백은 입력되지않음 
    printf("Reverse Alphabet : ");
    for(int i = 0, n = strlen(s); i < n; i++)
    {
        if(s[i] >= 'A' && s[i] <= 'Z')
        {
            printf("%c", tolower(s[i]));
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
