import random
from time import time
from Algorithm import  InsertionSort
from Algorithm import MergeSort
import matplotlib.pyplot as plt

n=1000
sizeArr =[]
insertionTime=[]
mergeTime=[]
arrayForMerge=[]

for i in range(n,n*11,n):
	sizeArr.append(i)
	randomValues = random.sample(range(i), i)
	arrayForMerge = randomValues
	startTime = time()
	InsertionSort(randomValues)
	endTime = time()
	totalTime = endTime -startTime
	insertionTime.append(totalTime)
	print("For",i,"the time in InsertionSort is",totalTime)

	startTime = time()
	MergeSort(arrayForMerge)
	endTime = time()
	totalTime = endTime -startTime
	mergeTime.append(totalTime)
	print("For",i,"the time in MergeSort is",totalTime)

fig,ax = plt.subplots(1,1)
ax.plot(sizeArr,insertionTime,label ='InsertionSort')
ax.plot(sizeArr,mergeTime,label ='MergeSort')
ax.legend(loc = 'upper center', fontsize = 'large')
plt.show()
