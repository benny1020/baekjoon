#include <iostream>
#include <cstring>

using namespace std;

int group_word(string str);

int main(void)
{
	int num;
	int total=0;
	string str="";
	cin >> num;
	
	for(int i=0;i<num;i++)
	{
		cin >> str;
		total+=group_word(str);
		str="";
		
	}
	
	cout << total;
	
	
	
	return 0;
	
}

int group_word(string str)
{
	int len = str.length();
	char ch[len]={'\0',};
	int n=0;	

	for(int i=1;i<len;i++)
	{
		if((str[i-1]!=str[i]))
		{
			ch[n]=str[i-1];
			for(int k=0;k<n;k++)
				if(str[i-1]==ch[k])
					return 0;
			n++;
			
			
		}
		if(i==len-1)
			for(int p=0;p<n+1;p++)
				if(str[len-1]==ch[p])
					return 0;
	}
	
	return 1;
	
}
