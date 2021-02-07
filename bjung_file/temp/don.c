#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int pay(int arr1[], char *arr2[]);

int size = 0;//명수

int main()
{
    char temp[100];//문자열을 입력 받기 위한 충분한 크기의 문자 배열을 선언한다.
    
    printf("명수를 입력하세요 : ");
    scanf("%d", &size);
    printf("-------------------------------------------\n");

    int *sizePtr = malloc(sizeof(int) * size);
    char *namePtr[size];

    for (int i = 0; i < size; i++)    // 입력받은 크기만큼 반복
    {
        printf("이름과 낸돈을 입력하세요 : ");
        scanf("%s %d", temp, &sizePtr[i]);     // 인덱스로 접근하여 값 할당
        namePtr[i] = (char *)malloc(strlen(temp) + 1);
        strcpy(namePtr[i], temp);//문자열 복사       
    }
    printf("-------------------------------------------");
    /*
    for (int i = 0; i < size; i++)    // 입력받은 크기만큼 반복
    {
        printf("%s %d\n", namePtr[i], sizePtr[i]);    // 인덱스로 접근하여 값 출력
    }
    */
    pay(sizePtr, namePtr);
}
    int pay(int arr1[], char *arr2[])
    {
        int allpay = 0;
        for(int i= 0; i < size; i++)
        {
            allpay += arr1[i];
        }

        printf("\n총합 금액은 %d원 입니다.\n", allpay);
        printf("1인당 지불할 금액은 %d원 입니다.\n",allpay / size);
        printf("-------------------------------------------\n");
        for(int i = 0; i <size; i++)
        {
            if (allpay / size < arr1[i]){printf("%s이 낼돈은 없습니다.\n", arr2[i]);}
            else {printf("%s이 낼돈은 : %d원 입니다.\n", arr2[i], allpay / size - arr1[i]);}
        }
        printf("-------------------------------------------\n");
        for(int i = 0; i <size; i++)
        {
            if((allpay / size) < arr1[i])
                printf("%s이 받을돈은 %d원 입니다.\n", arr2[i], arr1[i] - (allpay / size));    
            else
                printf("%s이 받을돈은 없습니다.\n", arr2[i]);
        }
        printf("-------------------------------------------\n");
        return 0;
    }