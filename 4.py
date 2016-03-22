r = 0

def isPalindrome(n):
	s=str(n)
	for i in xrange(0,len(s)/2):
		if s[i]!=s[len(s)-1-i]:
			return False
	return True

for a in xrange(100,1000):
	for b in xrange(100, 1000):
		if isPalindrome(a*b) and a*b>r:
			r=a*b
print r