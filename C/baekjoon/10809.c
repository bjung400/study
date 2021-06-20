#include <stdio.h>

int main(void)
{
    char S[101];
    int temp;
    scanf("%s", S);
    
    for (int i = 97; i <= 122; i++)
    {
        int count = 0;
        for (int j = 0; S[j] != (char)NULL; j++)
        {
            if (S[j] == i)
            {
                temp = count;
                break;
            }
            else
            {
                temp = -1;
            }
            count++;
        }
        printf("%d ", temp);    
    }
}