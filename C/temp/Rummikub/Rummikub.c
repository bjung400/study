#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct card
{
    int number; // 1 ~ 13
    int color; // 1 ~ 4
    int joker; // 2
};

void card_create(struct card c[104]);
void card_check(struct card c[104]);
void swap(struct card *a, struct card *b);
void shuffle(struct card *c);
void first_card(struct card c[104], struct card f[30]);

int main()
{
    struct card c[104];
    struct card user1[30];

    char select;

    card_create(c);
    shuffle(c);
    card_check(c);
    first_card(c, user1);

    printf("_____________________________________________________________\n");
    for (int i = 0; i < 14; i++)
    {
        if(user1[i].color == 1)
        {
            printf("\033[1;31m%d \033[0m", user1[i].number);
        }
        if(user1[i].color == 2)
        {
            printf("\033[1;34m%d \033[0m", user1[i].number);
        }
        if(user1[i].color == 3)
        {
            printf("\033[1;33m%d \033[0m", user1[i].number);
        }
        if(user1[i].color == 4)
        {
            printf("\033[1;30m%d \033[0m", user1[i].number);
        }
    }
    printf("\n----- select ----- \n d : Draw a card\n");
    scanf("%s", &select);
    if (select == 'd')
    {
         printf("----- Draw -----");
         user1[i+1]. = c[i+1]
         
    }
    
}

void card_create(struct card c[104])
{
    int n = 0;
    for (int i = 1; i <= 2; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            for (int k = 1; k <= 13; k++)
            {
                c[n].color = j;
                c[n].number = k;
                n++;
            }
        }
    }
}

void card_check(struct card c[104])
{
      for (int i = 0; i < 104; i++)
    {
        if (i < 104)
        {
            printf("color : %d, number : %d ", c[i].color, c[i].number);
        }
        else
        {
            printf("joker : %d ", c[i].joker);
        }
        printf(", count : %d\n", i + 1);
    }
}

void swap(struct card *a, struct card *b)
{
    struct card temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void shuffle(struct card *c)
{
    srand(time(NULL));
    int j;
    for (int i = 0; i < 104; i++)
    {
        j = rand() % 104;
        swap(c + i, c + j);
    }
}

void first_card(struct card c[104], struct card f[30])
{
    for(int i = 0; i < 14; i++)
    {
        f[i].color = c[i].color;
        f[i].number = c[i].number;
    }
}



