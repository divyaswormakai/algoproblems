def selectionSort(array: list) -> list:
	for i in range(len(array) - 1):
		minIndex = i
		for j in range(i + 1, len(array)):
			if array[j] < array[minIndex]:
				minIndex = j
		array[i], array[minIndex] = array[minIndex], array[i]


if __name__ == '__main__':
	# array = random.sample(range(1, 1000), 500)
	array = [5, 3, 2, 10 , 1 , 9]
	selectionSort(array)
	print(array)
	