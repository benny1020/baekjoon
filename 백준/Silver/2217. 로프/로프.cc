#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int n, inp;
    vector<int> arr;
    cin >> n;
    while(n--) {
        cin >> inp;
        arr.push_back(inp);
    }

    sort(arr.begin(),arr.end());

    int weight = arr.back();
    int num = 1;
    arr.pop_back();
    for(int i=arr.size()-1;i>=0;i--) {
        num+=1;
        if(weight < arr[i]*num) {
            weight = arr[i]*num;
        }
    }
    cout << weight << endl;
    return 0;

}