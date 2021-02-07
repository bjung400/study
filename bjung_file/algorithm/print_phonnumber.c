#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[] = {"jong","byungwook","sss","suck"};
    string numbers[] = {"010-3700-6377", "010-5064-4165", "010-1234-6366", "010-9876-6377"};

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(names[i], "jong") == 0)
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}

