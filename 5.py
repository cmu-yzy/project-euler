n = 20
l=[]
p=1

# generate priem list
def nextPrime():
	global p,l
	while True:
		p+=1
	 	if isPrime():
	 		break

def isPrime():
	global p,l
	for x in l:
		if p%x==0:
			return False
	return True

while True:
	nextPrime()
	if p>n:
		break
	l.append(p)

# count 
cnt=[0]*len(l)

for i in xrange(1,n+1):
	for j in xrange(0,len(l)):
		c=0
		while i%l[j]==0:
			c+=1
			i/=l[j]
		cnt[j]=max(c,cnt[j])

# aggregate
r=1

for i in xrange(0,len(l)):
	r*=l[i]**cnt[i]

print r