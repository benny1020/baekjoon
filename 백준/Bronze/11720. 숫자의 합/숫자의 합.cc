#include <iostream>

using namespace std;

int main(void)
{
	int num;
	char ch;
	cin >> num;
	int temp;
	int k=0;
	for(int i=0;i<num;i++)
	{
		cin >> ch;
		k=k+(int)ch-48;
		temp+=k;
		
	}
	cout << k;
	return 0;
}