def fibrecur(n):
	if(n<=1):
		return n
	else:
		res = fibrecur(n-1)+fibrecur(n-2)
	return res

memoArr = [None] * (100)
def fibmem(n):
	if memoArr[n]!=None:
		return memoArr[n]
	elif(n<=1):
		result = n
	else:
		result = fibmem(n-1) + fibmem(n-2)
	memoArr[n] = result
	return result

def fibtabu(n):
	if(n<=1):
		return n
	else:
		arr = [0]*(n+1)
		arr[1]=1
		for i in range(2,n+1):
			arr[i] = arr[i-1]+arr[i-2]

		return arr[n]

print(fibrecur(5))
print(fibmem(5))
print(fibtabu(5))