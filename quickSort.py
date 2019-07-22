def parti(arr,low,high):
	 i = low-1
	 pivot = arr[high]

	 for j in range(low,high):
	 	if arr[j] <=pivot:
	 		i+=1
	 		arr[i],arr[j] = arr[j],arr[i]
	 arr[i+1],arr[high] = arr[high],arr[i+1]
	 return i+1

def quick(arr,low,high):
	if(low<high):
		pivot = parti(arr,low,high)

		quick(arr,low,pivot-1)
		quick(arr,pivot,high)


if __name__ == '__main__':
	arr=[2, 5, 1, 3, 2, 4, 6]
	n = len(arr) 
	quick(arr,0,n-1) 
	print ("Sorted array is:") 
	for i in range(n): 
   		print ("%d" %arr[i]), 