X = "okhaldhunga"
Y="kathmandu"
def lcs(X,Y,m,n):
	if m == len(X) or n == len(Y):
		return 0
	elif X[m] == Y[n]:
		return 1 + lcs(X, Y, m+1, n+1)
	else:
		return max(lcs(X, Y, m, n+1), lcs(X, Y, m+1, n))

print(lcs(X,Y,0,0))