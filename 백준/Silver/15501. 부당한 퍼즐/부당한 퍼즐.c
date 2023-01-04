#include <stdio.h>

typedef struct 
{
    int data;
    struct Node * next;
    struct Node * before;
} Node;

int main(void)
{
    int num;
    scanf("%d", &num);
    int arr[num];
    int tarr[num];
    for (int i = 0; i < num; i++)
        scanf("%d", &arr[i]);

    for (int i = 0; i < num; i++)
        scanf("%d", &tarr[i]);
    if(num==1)
        {
            printf("good puzzle\n");
            return 0;
        }

    Node *start = (Node *)malloc(sizeof(Node));
    Node * tmp = start;
    start->data = arr[0];

    Node * finish;
    for(int i = 1; i < num; i++)
    {   
        Node * new_node = (Node * )malloc(sizeof(Node));
        if(i == num-1)
            finish = new_node;
        new_node->data = arr[i];
        new_node->before = tmp;
        tmp->next = new_node;
        tmp = tmp->next;
    }
    start->before = finish;
    


    finish->next = start;
    start->before = finish;


    int t1 = 1;
    int t2 = 1;

    tmp = start;
    while(tmp->data != tarr[0])
        tmp = tmp->next;
    
    for(int i=0; i<num; i++) //안뒤집힌경우
    {
        if(tmp->data != tarr[i])
        {
            t1 = 0;
            break;
        }
        else
        {
            tmp = tmp->next;
        }
                
    }

    while (tmp->data != tarr[0])
        tmp = tmp->next;
    for (int i = 0; i < num; i++) //뒤집힌경우
    {
        if (tmp->data != tarr[i])
        {
            t2 = 0;
            break;
        }
           
        else
        {
            tmp = tmp->before;
        }
    }

    if(t1 == 1 || t2 == 1)
        printf("good puzzle\n");
    else
    {
        printf("bad puzzle\n");
    }
    
    return 0;

    
}