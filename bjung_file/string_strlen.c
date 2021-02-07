//#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[1000];
    printf("출력할 문자열을 입력하세요\n");
    scanf("%s", s);
    //string s = get_string("input : ");
    printf("Output\n");
    //strlen 함수로 문자열 길이 저장후 길이만큼 for문 순환
    for (char i = 0, n = strlen(s); i < n; i++)
    {
        printf("%i : ", i);
        printf("%c\n", s[i]);
    }
}

