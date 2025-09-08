def gcd(a,b):
	if b==0: return a
	return gcd(b,a%b)
def lcm(a,b):
	return a*b//gcd(a,b)
def etf(n):
	nn = n
	res = n
	k = 2
	while nn!=1:
		if nn == n and k*k >n:
			return n-1
		if nn%k==0:
			res = res*(k-1)//k
			while nn%k==0:
				nn//=k
		k = k+1
	return res




