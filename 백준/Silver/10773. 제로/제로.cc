
#include <iostream>

using namespace std;

int main(void)
{
    int num;
    int zeros=0;
    int total=0;
    cin >> num;
    int * dp = new int[num];
    for(int i=0;i<num;i++)
        cin >> dp[i];

    for(int i=num-1;i>=0;i--)
    {
        if(dp[i] == 0)
            zeros++;
        else
        {
            if(zeros == 0)
                total+=dp[i];
            else
                zeros--;
        }
    }
    cout << total << endl;
    return 0;
}
