#include <iostream>

using namespace std;

int main(void)
{
	int N, M;
	int max=0;

	cin >> N;
	cin >> M;

	int * arr = new int[N];

	for(int i=0; i < N; i++)
		cin >> arr[i];

	for(int i=0;i<N-2;i++)
		for(int k=i+1;k<N-1;k++)
			for(int j=k+1;j<N;j++)
				if(arr[i]+arr[k]+arr[j]<=M)
				{	
				
					if(arr[i]+arr[k]+arr[j]>=max)
				
						max=arr[i]+arr[k]+arr[j];
				}
	cout << max;

	return 0;

}