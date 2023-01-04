#include <iostream>
#include <cstring>

#define MAX_SIZE 1000000
using namespace std;

int main(void)
{
	string str;
	
	string space;
	space = " ";
	getline(cin,str,'\n');
	
	int num=0;
	int len=str.length();
	
	for(int i=1;i<len-1;i++)
	{	
		
		if(str[i]==' ')
			num++;
	}
	if(str.compare(space)==0)
		num=-1;
	cout << num+1;
	
}