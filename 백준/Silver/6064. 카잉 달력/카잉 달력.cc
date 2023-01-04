#include <iostream>

using namespace std;

int main(void)
{
    int num;
    int N, M, x, y;
    int a,b;
    int count;
    int max_c=0;
    cin >> num;
    for(int i=0;i<num;i++)
    {
        cin >> N >> M >> x >> y;
        bool is_true = true;
        a=1;
        b=1;
        count =N;
        a=N;
        b=N%M;
        if(b==0)
            b=M;
        while( !(a == N && b == M) )
        {
            b+=N;
            b = b%M;
            if(b==0)
                b=M;
            count+=N;
        }
        max_c = count;
        count = x;
        a = x;
        b = x;
        b %=M;
        if(b==0)
            b=M;
        while( !(a == x && b == y ))
        {
            count+=N;
            b+=N;
            b %=M;
            if(b==0)
                b=M;
            if(count > max_c)
            {
                is_true = false;
                break;
            }
        }
        if(is_true == false)
            cout << -1 << endl;
        else
            cout << count << endl;
    }
    return 0;
}