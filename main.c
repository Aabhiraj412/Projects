#include<stdio.h>

int main(int argc, char const *argv[])
{
    int a, b;

    printf("Please Enter 1st Number -> ");
    
    scanf("%d", &a);

    printf("Please Enter 2nd Number -> ");

    scanf("%d", &b);

    printf("Sum of Two Numbers is -> %d\n", a + b);

    printf("Difference of Two Numbers is -> %d\n", a - b);
    
    printf("Multiplication of Two Numbers is -> %d\n", a * b);
    
    printf("Devision of Two Numbers is -> %d\n", a / b);
    

    return 0;
}

