#include <iostream>
using namespace std;

int main()
{
  ///////////////변수 선언 부분/////////////
  int num,i,a;
  int max=0,sum=0;
  /////////////입력/합계/번호 판별 부분//////
  for(i=0;i<5;i++)
  {
    sum=0;
    for(int j=0;j<4;j++){cin>>num; sum+=num;}
    if(max<sum){max=sum; a=i;}
  }
  //////////// 우승자 번호 및 점수 출력 부분 //////////
  cout<<a+1<<" "<<max<<endl;
}