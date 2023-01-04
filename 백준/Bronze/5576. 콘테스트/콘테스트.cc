
#include <iostream>

using namespace std;

void sort(int * arr, int num)
{
    for(int i=0;i<num-1;i++)
        for(int j=0;j<num-i;j++)
        {
            if(arr[j]>arr[j+1])
            {
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
        }
}

int main(void)
{
    int num = 10;
    int total_w=0;
    int total_k=0;
    int w_arr[num];
    int k_arr[num];

    int input;
    for(int i=0;i<num;i++)
        cin >> w_arr[i];

    for(int i=0;i<num;i++)
        cin >> k_arr[i];

    sort(w_arr,num);
    sort(k_arr,num);

    total_w = w_arr[num-1]+w_arr[num-2]+w_arr[num-3];
    total_k = k_arr[num-1]+k_arr[num-2]+k_arr[num-3];

    cout << total_w << " " << total_k << endl;

    return 0;
}