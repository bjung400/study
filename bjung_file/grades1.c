#include<stdio.h>

int main(){

    char* grade[9] = {"A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"};
    int score[9] = {95, 90, 85, 80, 75, 70, 65, 60, 0};
    int i, usr;

    printf("학점 프로그램\n종료를 원하면 \"999\"를 입력\n");
    printf("점수: ");
    for(i=0; i<9; i++){
        printf("%d\t", score[i]);
    }
    printf("\n학점: ");
    for(i=0; i<9; i++){
        printf("%s\t", grade[i]);
    }
    printf("\n");
    
    while(1){
        printf("성적을 입력하세요 (0 ~ 100) : ");
        scanf("%d", &usr);

        if(usr == 999) {
            printf("학점 프로그램을 종료합니다.\n");
            break;
        }
        else if (usr>100 || usr<0) {
            printf("** %d 성적을 올바르게 입력하세요. 범위는 0 ~ 100 입니다.\n", usr);
        }
        else{
            for(i=0; i<9; i++){
                if(usr >= score[i]) {
                    printf("학점은 %s 입니다.\n", grade[i]); 
                    break;
                }
            }
        }
    }
    return 0;
}