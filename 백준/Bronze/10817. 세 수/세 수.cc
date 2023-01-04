#include <iostream>

using namespace std;

int main(void)
{
    int a, b, c, tmp;
    cin >> a >> b >>c ;
    if(a >=b)
    {
        tmp = a;
        a= b;
        b= tmp;
    }
    if(b>=c)
    {
        tmp = c;
        c=b;
        b=tmp;
    }
    if(a >=b)
    {
        tmp = a;
        a= b;
        b= tmp;
    }
    if(b>=c)
    {
        tmp = c;
        c=b;
        b=tmp;
    }
    cout << b<<endl;
    return 0;
    
}