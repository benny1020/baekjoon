#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  char num[100000];

  while(1){
    int cnt=0;
    int a=0;

    cin>>num;

    if (strlen(num)%2==0){a=strlen(num)/2;}
    else{a=strlen(num)/2+1;}

    if(num[0]=='0'){break;}

    for (int i=0;i<=a;i++){
      if(num[i]!=num[strlen(num)-(i+1)]){
        cout<<"no"<<endl;
        break;}
      else if (num[i]==num[strlen(num)-(i+1)]) {cnt++;}
    }

    if((cnt-1)==a){cout<<"yes"<<endl;}

  }

}