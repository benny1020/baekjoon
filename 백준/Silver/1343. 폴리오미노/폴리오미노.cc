#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void) {
    string str;

    cin >> str;

    vector<char> arr;

    int cnt=0;
    for(int i=0;i<str.length();i++) {
        if(str[i] == 'X') 
            cnt++;
        else {
            if(cnt%2==1) {
                cout << -1 << endl;
                return 0;
            }
            for(int j=0;j<(cnt/4);j++ ){
                for(int t=0;t<4;t++)
                    arr.push_back('A');
            }
            for(int j=0;j<(cnt - (cnt/4)*4)/2;j++) {
                for(int t=0;t<2;t++)
                    arr.push_back('B');
            }
            arr.push_back('.');
            cnt = 0;
        }
    }
    //문자열 끝난경우
    if(cnt > 0) {
        if(cnt%2 == 1) {
            cout << -1 << endl;
            return 0;
        }
        for(int j=0;j<(cnt/4);j++ ){
                for(int t=0;t<4;t++)
                    arr.push_back('A');
            }
            for(int j=0;j<(cnt - (cnt/4)*4)/2;j++) {
                for(int t=0;t<2;t++)
                    arr.push_back('B');
            }
    }

    for(int i=0;i<arr.size();i++)
        cout << arr[i];

    cout << endl;
}