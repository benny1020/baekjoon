#include <stdio.h>

int main(void)
{
    int tnum;
    int count=0;
    int div;
    int arr[] = {500, 100, 50, 10, 5, 1};

    scanf("%d", &tnum);
    int num = 1000-tnum;
    for(int i=0; i<7; i++)
    {
        div = arr[i];
        int temp = num/div;
        num = num - temp*div;
        count +=temp;
    }
    printf("%d", count);

}