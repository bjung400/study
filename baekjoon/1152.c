#include <stdio.h>
#include <string.h>

int main()
{
    char str[1000003];
    int count = 0;

    scanf("%[^\n]", str);
    
    if(strlen(str) == 1)
    { 
        if(str[0] == ' ')
        { 
            printf("0\n");
            return 0; 
        }
    }

    for(int i = 0; i < str[i] != '\0'; i++)
    {
        if(str[i] != ' ' && str[i+1] == ' ')
        {
            count += 1;
        }         
    }
    if(str[0] == ' ') count--;
    if(str[strlen(str)-1] == ' ') count--;
    printf("%d", count + 1);
}