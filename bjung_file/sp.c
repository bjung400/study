#include <stdio.h>

int main()
{
    int H, M;
    scanf("%d %d", &H, &M);
    if(0 <= H <= 23 && 0 <= M <= 59)
    {
        if(M < 45)
        {
            if(H == 0)
            {
                H = 23;
            }
            else
            {
                H -= 1;
                M = M + 15;
            }
        }
        else
        {
            M -= 45;

            printf("%d %d", H, M);
        }
    }
    else
    {
        printf("잘못된 값이 입력되었습니다.");
    }
}