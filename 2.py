r=0
a=1
b=2
while b<=4000000:
	if b%2==0:
		r=r+b
	a,b=b,a+b
	print a,b,r