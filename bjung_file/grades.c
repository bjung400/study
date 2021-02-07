#include <stdio.h>

int scores(int in);
const int NUMBER_OF_GRADES = 9;
const int SCORES[NUMBER_OF_GRADES] = {95, 90, 85, 80, 75, 70, 65, 60, 0};
const char *GRADES[NUMBER_OF_GRADES] = {"A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"};
int input = 0;

int main(void)
{
    printf("학점 프로그램\n종료를 원하면 \"999\" 를 입력\n");
    printf("[학점 테이블]\n");
    printf("점수 : ");
    for(int i = 0; i < NUMBER_OF_GRADES; i++){printf("%d\t", SCORES[i]);}
    printf("\n학점 : ");
    for(int i = 0; i < NUMBER_OF_GRADES; i++){printf("%s\t", GRADES[i]);}
    printf("\n");

    while(1)
    {
        printf("성적을 입력하세요 (0 ~ 100) : ");
        scanf("%d", &input);
        if(input == 999)
        {
            printf("학점 프로그램을 종료합니다.\n");
            break;
        }
        scores(input);
    }
    return 0;
}

int scores(int in)
{
    if(0 <= in && in <= 100)
            {
                for(int i = 0; i < NUMBER_OF_GRADES; i++)
                {
                    if(input >= SCORES[i])
                    {
                        printf("학점은 %s 입니다.\n", GRADES[i]);
                        break;
                    }
                }
            }
    else
            printf("** %d 성적을 올바르게 입력하세요. 범위는 0 ~ 100 입니다.\n", input);
    return 0;
}