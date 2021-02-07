#include <stdio.h>

int main(void)
{
    // Scores
    int score[3];
    score[0] = 72;
    score[1] = 73;
    score[2] = 33;

    // Print average
    printf("Average : %d \n", (score[0] + score[1] + score[2]) / 3);
}
