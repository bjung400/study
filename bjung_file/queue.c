#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_QUEUE_COUNT 100 //출처: http://www.tipssoft.com/bulletin/board.php?bo_table=
int main(void)
{
    int menu, data;
    int i = 0;
    int q_data[MAX_QUEUE_COUNT];
    // 큐에서 가장 먼저 처리될 자료의 앞 인덱스를 저장하는 변수
    int front = -1;
    
    int rear = -1;// 큐의 마지막에 저장된 자료의 인덱스를 저장하는 변수 
    
    printf("CS50 과제 3 Queue를 만들어보자!!\n\n");
    printf("< 메뉴 > \n");
    printf("1 : AddQueue 큐에 값을 추가\n");
    printf("2 : DeleteQueue 큐에 값을 제거 \n");
    printf("3 : display 큐에 값을 나열 \n");
    printf("4 : 프로그램 종료 \n\n");
    while (1){
        printf("\n메뉴 선택 : ");
        scanf("%d", &menu);
        if (1 == menu){
        if (rear != MAX_QUEUE_COUNT - 1){
            printf("큐에 넣을 값 : ");
            scanf("%d", &data);
            // 큐의 마지막 자료 다음에 데이터를 추가
            q_data[++rear] = data;
            i++;
        } else {
            // 큐가 Full 인 경우
            printf("더 이상 큐에 자료를 넣을 수 없습니다.\n");
            }
        }
        else if (2 == menu){
            if (rear != front){
        // Front 값에 다음 인덱스를 저장
        front++;
        data = q_data[front];
        printf("큐에서 처리된 데이터 : %d\n", data);
        i=i-1;
        }
        else {
        // 큐가 Empty 인 경우
        printf("큐에 데이터가 존재하지 않습니다.\n");
        }
        }
        else if (3 == menu){
        if (rear != front){
            // queue 내용물을 출력
            for(int q = 0; q < i; q++)
            {
            printf("저장된 데이터%i : %d\n", q+1, q_data[front+1+q]);
            }
        }      
        else {
            // 큐가 Empty 인 경우
            printf("큐에 데이터가 존재하지 않습니다.\n");
            }
        }
        else if (4 == menu){
            printf("\n큐 프로그램을 종료합니다.\n");
            break;
        }
    }
}