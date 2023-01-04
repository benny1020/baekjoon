#include <iostream>


using namespace std;

int main(void)
{
	int num;
	int temp;
	cin >> num;
	
	int arr[num];
	
	for(int i=0;i<num;i++)
	{
		cin >> arr[i];
	}
	

	for(int t=num;t>0;t--)
	{
		for(int k=0;k<t-1;k++)
		{	
	
			if(arr[k]>arr[k+1])
			{	
				temp = arr[k];
				arr[k]=arr[k+1];
				arr[k+1]=temp;
			}	
		}
	
	}
	

	

	int total=0;
	for(int i=0;i<num;i++)
	{
		total+=arr[i]*(num-i);
		
	}
	cout << total;
	
	return 0;
}