#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    int ans = 0;
    ans += (n/5);
    n = n-5*(n/5);
    if(n%2 == 1) {
        if(ans==0)
            cout << -1 << endl;
        else {
            cout << ans-1+((n+5)/2) << endl;
        }
        return 0;
    }
    ans += n/2;
    cout << ans<<endl;
    return 0;

}