#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
    int num;
    int res = 0;
    cin >> num;
    int digit = 1;
    int dec = 10;

    while(num/dec >= 1 )
    {
        dec *=10;
        digit++;
    }
    for(int i=1;i<digit;i++)
    {
        res += ((pow(10,i)-pow(10,i-1)))*i;
    }
    res +=((num-pow(10,digit-1)+1)*digit);
    cout << res << endl;
    return 0;
}
