#include <iostream> //맞은 코드
using namespace std;
int main(void){
    long long n;
    while(cin >> n){ //차이점
        long long first = 1;
        long long count = 1;
        while(1){
            first = first % n;
            if(first == 0){
                break;
            }
            first = (first * 10)%n + 1%n;
            count++;
        }
        cout << count << '\n';
    }
}