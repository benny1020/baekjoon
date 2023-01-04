#include <iostream>
using namespace std;
void sol(int num)
{
    //num *=100;
    cout << num/25 << " ";
    num = num - (num/25)*25;
    cout << num/10 << " ";
    num = num - (num/10)*10;
    cout << num/5 << " ";
    num = num - (num/5)*5;
    cout << num/1 <<endl;
}

int main(void)
{
    int num;
    int tmp;
    cin >> num;
    for(int i=0;i<num;i++)
    {
        cin >> tmp;
        sol(tmp);
    }
    return 0;
}