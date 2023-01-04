#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    vector<int> oil;
    vector<int> city;
    int inp;
    for(int i=0;i<n-1;i++) {
        cin >> inp;
        oil.push_back(inp);
    }
    for(int i=0;i<n;i++) {
        cin >> inp;
        city.push_back(inp);
    }
    city.pop_back();

    int total = 0;
    int min_oil;
    for(int i=city.size()-1;i>=0;i--) {
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