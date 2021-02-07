#include <stdio.h>

#define MAXSIZE 10
int stack[MAXSIZE];
int top;

int push(unsigned int val) {
    if (top >= MAXSIZE-1) {
        printf("Stack Overflow.");
        return -1;
    }
    stack[++top] = val;
    return val;
}

int pop(void) {
    if (top < 0) {
        printf("Stack Underflow.");
        return -1;
    }
    return stack[top--];
}


int main(void)
{
    int i;s
    int j;
    int k;
    top = -1;
    
    push(5);
    push(4);
    i = pop();
    j = pop();
    push(7);
    printf("%d, %d\n", i, j);
    for( k = top; k >= 0; k--)
      printf("%d, ", stack[k]);
}