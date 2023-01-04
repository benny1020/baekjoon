/*
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi
예제 출력 1 
?
예제 입력 2 
zZa
예제 출력 2 
Z
예제 입력 3 
z
예제 출력 3 
Z
예제 입력 4 
baaa
예제 출력 4 
A

대문자 + 32 = 소문자;

a 97 A 65

*/	
#include <iostream>
#include <cstring>

#define MAX_SIZE 1000000
using namespace std;


int biggest(int * arr);
int main(void)
{
	int len;
	
	int arr[26]={0,};
	
	char ch[MAX_SIZE] = {'\0',};
	
	cin >> ch;
	len = strlen(ch);
	
	for(int k='a';k<='z';k++)
	{
		for(int p=0;p<len;p++)
		{
			if(ch[p]==k)
				arr[(int)k-97]++;
		}
	}
	
	for(int k='A';k<='Z';k++)
	{
		for(int p=0;p<len;p++)
		{
			if(ch[p]==k)
				arr[(int)k-65]++;
		}
	}
	
	
	int pp = biggest(arr);
	if(pp==-1)
		cout << '?';
	else
		cout << (char)(pp+65);
	
}

int biggest(int * arr)
{
	int max=0;
	int max_num;
	int num=0;
	for(int i=0;i<26;i++)
		if(max<arr[i])
			max=arr[i], max_num=i;
	
	for(int i=0;i<26;i++)
		if(max==arr[i])
			num++;
	
	if(num>=2)
		return -1;
	else
		return max_num;
}
