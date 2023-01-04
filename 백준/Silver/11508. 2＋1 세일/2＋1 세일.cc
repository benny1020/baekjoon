#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
    int n, inp;
    cin >> n;
    vector<int> arr;

    while(n--) {
        cin >> inp;
        arr.push_back(inp);
    }
    sort(arr.begin(),arr.end());

    int total= 0;
    int tmp=0;
    for(int i=arr.size()-1;i>=0;i--) {
        if(tmp==2) {
            tmp=0;
            continue;
        }
        total+=arr[i];
        tmp++;
    }
    cout << total << endl;

    return 0;
    
}