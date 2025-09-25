def GCD(a,b):
	if b == 0:
		return a
	else:
		return GCD(b,a%b)

def euclideExtend(a,b):
	def recursion(a,b):	
		if b==0:
			return a,1,0
		gcd,x1,y1 = recursion(b,a%b)
		x = y1
		y = x1 - (a//b)*y1
		return gcd,x,y
	result = recursion(a,b)
	return (result[1],result[2])

#Euler's Totient Function
def ETF(n):
	n2 = n
	res = n
	if n%2 == 0:
		res = res//2
		while n%2 == 0:
			n = n//2
	p = 3
	while n!=1:
		if n%p == 0:
			res = res - res//p
			while n%p == 0:
				n = n//p
		p = p+2
		if p**2 > n2 and n == n2:
			return n-1 
	return res
def modularInverse(a,m):
	if m<2 or a == 0:
		return None
	tup = euclideExtend(a,m)
	if tup[0]*a%m == 1:
		return tup[0]%m
	else:
		return None
def CRT(a,m):
	if len(a) != len(m):
		return None
	M = 1
	for i in range(len(m)):
		a[i] = a[i]%m[i]
		M *= m[i]
	x = 0
	for i in range(1,len(a)+1):
		ai = a[i-1]
		mi = m[i-1]
		pi = M//mi
		pi_inv = modularInverse(pi,mi)
		x += ((ai*pi*pi_inv))
	return x



