#include <stdio.h>

void draw(int h);
int h = 0;
int count;
int main(void)
{
    printf("Height: ");
    scanf("%d", &h);
    int height = h;

    draw(height);
}

void draw(int h)
{
    printf("호출");
    // 높이가 0이라면 (그릴 필요가 없다면)
    if (h == 0)
    {
        return;
    }

    // 높이가 h-1인 피라미드 그리기
    draw(h - 1);

    // 피라미드에서 폭이 h인 한 층 그리기
    for (int i = 0; i < h; i++)
    {
        printf("#");
    }
    printf("\n");
}