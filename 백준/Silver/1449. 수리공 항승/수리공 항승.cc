#include <iostream>

using namespace std;

int main(void)
{
    int num;
    int tape_len;
    int tmp;
    int tape_num=0;
    cin >> num >> tape_len;
    int arr[1001];
    for(int i=0;i<1001;i++)
        arr[i] = 0;

    for(int i=0;i<num;i++)
    {
        cin >> tmp;
        arr[tmp] = 1;
        arr[tmp-1] = 1;
    }
    // 0 1 2

    for(int i=0;i<1001;i++)
    {
        if(arr[i] == 1)
        {
            tape_num++;
            for(int j=0;j<=tape_len;j++)
            {
                if(i+j==1001)
                    break;
                arr[i+j]=0;
            }
            i=i+tape_len-1;
        }
    }
    cout << tape_num << endl;
    return 0;
}