#include <iostream>
#include <cmath>

using namespace std;

int BE_Point(int fixed_price, int changed_price, int sell_price); 

int main()
{
	int a,b,c;
	cin >> a >> b >> c;

	int ptr = BE_Point(a,b,c);
	
	cout << ptr;
	

	
	return 0;
}

int BE_Point(int fixed_price, int changed_price, int sell_price)
{

	
	int m = sell_price-changed_price;
	
	if(m <= 0 )
		return -1;
	

	return fixed_price/m+1;
		
		
}