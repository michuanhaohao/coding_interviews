# [Ebay]
'''
Given x and n, realize function pow(x,n)
'''

def power(x, n):
	if n == 0:
		return 1
	if n < 0:
		x = 1.0/x
		n = -n

	return power(x*x, n/2) if n%2 == 0 else power(x*x, n/2)*x


if __name__ == "__main__":
	exs =[ [5,-1], [2, 11], [5,1]]
	for ex in exs:
		print "input:"
		print ex
		print "output:"
		print(power(ex[0],ex[1]))

	 
