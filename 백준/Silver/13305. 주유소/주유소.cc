#include <iostream>
#include <vector>

using namespace std;


int main(void) {
    int n;
    long long int total=0;
    cin >> n;
    vector<long long int> oil;
    vector<long long int> city;
    long long int inp;
    // --------- 입력 처리
    for(int i=0;i<n-1;i++) {
        cin >> inp;
        oil.push_back(inp);
    }
    for(int i=0;i<n;i++) {
        cin >> inp;
        city.push_back(inp);
    }
    city.pop_back();

    long long int minn = city[0];
    total = minn*oil[0];
    for(int i=1;i<oil.size();i++) {
        if(minn > city[i])
            minn = city[i];
        total += minn*oil[i];
    }
    cout << total << endl;
    return 0;
}
/* 반대쪽부터 풀려다 시간초과로 망함 안그래도 되는데 
int main(void) {
    int n;
    cin >> n;
    vector<long long int> oil;
    vector<long long int> city;
    long long int inp;
    // --------- 입력 처리
    for(int i=0;i<n-1;i++) {
        cin >> inp;
        oil.push_back(inp);
    }
    for(int i=0;i<n;i++) {
        cin >> inp;
        city.push_back(inp);
    }
    city.pop_back();
    // ----------------

    long long int total = 0;
    long long int min_oil;
    for(int i=oil.size()-1;i>=0;i--) {
        min_oil = city[0];
        for(int j=0;j<city.size();j++) {
            if(min_oil>city[j])
                min_oil = city[j];
        }
        total += min_oil*oil.back();
        oil.pop_back();
        city.pop_back();
    }
    cout << total << endl;
    return 0;
        
}
*/