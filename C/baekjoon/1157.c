#include <stdio.h>

int main()
{
    char str[1000001];
    int alphabet[26] = {0, };
    int max = 0, max_index = 0;

    scanf ("%s", str);

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] >= 'a' && str[i] <= 'z')
        {
            str[i] -= 32;
        }
        alphabet[str[i] - 65]++;
    }

    for (int i = 0; i < 26; i++)
    {
        if (alphabet[i] > max)
        {
            max = alphabet[i];
            max_index = i;
        }
        else if (max == alphabet[i] && alphabet[i] != 0)
        {
            max_index = -2;
        }
    }
        printf("%c", max_index + 65);
}