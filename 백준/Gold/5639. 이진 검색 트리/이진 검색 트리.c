#include <stdio.h>
#include <stdlib.h>

#define MAX_NUM 10000

typedef struct
{
    int data;
    struct Node * leftChild;
    struct Node * rightChild;
} Node;

Node * initNode(int data)
{
    Node * node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->leftChild = NULL;
    node->rightChild = NULL;

    return node;
}

void PostOrder(Node * node)
{
    if(node==NULL)
        return;
    PostOrder(node->leftChild);
    PostOrder(node->rightChild);
    printf("%d\n",node->data);
}

void insert_node(Node * root, Node * new_node)
{
    if(root == NULL)
    {
        root = new_node;
        return;
    }
    Node * tmp = root;
    while(1)
    {
        if(tmp->data > new_node->data)
        {
            if(tmp->leftChild==NULL)
            {
                tmp->leftChild = new_node;
                return;
            }
            else
                tmp = tmp->leftChild;
        }

        else
        {
            if(tmp->rightChild==NULL)
            {
                tmp->rightChild = new_node;
                return;
            }
            else
                tmp = tmp->rightChild;
        }
    }
}


int main(void)
{
    int arr[MAX_NUM];
    int num, root_num;
    num=1;

    scanf("%d",&arr[1]);
    Node * root = initNode(arr[1]);
    num++;
    while(~scanf("%d",&arr[num])) { 
        Node * new_node = initNode(arr[num]);        
        insert_node(root, new_node);
        num++;
    }
    PostOrder(root);
    
    return 0;
}
