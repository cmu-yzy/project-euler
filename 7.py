l=[]
p=1

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

for i in xrange(0,10001):
	nextPrime()

print l[-1]