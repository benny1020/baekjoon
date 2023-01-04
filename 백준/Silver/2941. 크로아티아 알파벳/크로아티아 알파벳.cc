#include <iostream>
#include <cstring>
#include <cstdio>



using namespace std;

int str_find_num(string str, string str_find);

int main(void)
{
	string str1;
	int size_num=0;
	int num;
	
	
	cin >> str1;
	

	

	
	size_num=str1.size();
	
	num=str_find_num(str1,"c=");
	size_num-=num;
	//cout<<"c=" << num<< endl;
	num=str_find_num(str1,"c-");
	size_num-=num;
	//cout<<"c-=" << num<< endl;
	num=str_find_num(str1,"dz=");
	size_num-=num;
	//cout<<"dz=" << num<< endl;
	num=str_find_num(str1,"d-");
	size_num-=num;
	//cout<<"d-" << num<< endl;
	num=str_find_num(str1,"lj");
	size_num-=num;
	//cout<<"lj=" << num<< endl;
	num=str_find_num(str1,"nj");
	size_num-=num;
	//cout<<"nj" << num<< endl;
	num=str_find_num(str1,"s=");
	size_num-=num;
	//cout<<"s=" << num<< endl;
	num=str_find_num(str1,"z=");
	size_num-=num;
	//cout<<"z=" << num<< endl;
	
	cout << size_num;
	
}


int str_find_num(string str, string str_find)
{
	int num=0;
	int total=0;
	num=str.find(str_find);
	int i=0;
	num = str.find(str_find);
	if(num>=0)
		total++;
	i=num;
	while(num>=0)
	{
		
		num=str.find(str_find,i+1);
		i=num;
	
		if(i>=0)
		{
			total++;
			
		}
	}
	return total;
}