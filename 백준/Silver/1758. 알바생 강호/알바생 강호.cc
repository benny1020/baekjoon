#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {
    long long int n, inp;
    vector<long long int> tips;
    cin >> n;
    while(n--) {
        cin >> inp;
        tips.push_back(inp);
    }
    sort(tips.begin(),tips.end());
    long long int total = 0;
    long long int start = 1;
    for(long long int i=tips.size()-1;i>=0;i--) {
        if(tips[i]-(start-1)>=0)
            total += tips[i]-(start-1);
        start++;
        tips.pop_back();
    }
    cout << total << endl;
    return 0;
    
}