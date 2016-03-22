l=[]
p=1
n=600851475143

def nextPrime():
	global p,l
	while True:
		p+=1
	 	if isPrime():
	 		l.append(p)
	 		break

def isPrime():
	global p,l
	for x in l:
		if p%x==0:
			return False
	return True

while n!=1:
	nextPrime()	
	while n%p==0:
		n/=p

print l
