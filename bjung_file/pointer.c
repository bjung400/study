#include <stdio.h>

int main(void)
{
    int **p;
    int a = 5;

    *p = &a;

    printf("%d \n", a);
    printf("%d \n", **p);
    return 0;
}