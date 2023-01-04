count=0
money=0
a=[]
total=0
p=0
count,money = map(int,input().split())



p=int(p)
while len(a)<count:
	a.append(int(input()))

	
	
for i in range(count):
	p = money//a[count-i-1]
	money = money-(p*a[count-i-1])
	total = total + p
	

	
	
	
	
		
		
print(total)

