#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
    person;

int main(void)
{
    person people[4];

    people[0].name = "byungwook";
    people[0].number = "010-5064-4165";
    people[1].name = "suck";
    people[1].number = "010-1234-4165";
    people[2].name = "jong";
    people[2].number = "010-3700-6377";
    people[3].name = "sss";
    people[3].number = "010-9865-4165";

    // jong 검색
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, "byungwook") == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}

