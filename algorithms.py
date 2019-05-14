from math import log

#BigTheta(n) function used to get a baseline time comparison
def baseline(arg):
	i = 0
	for elem in range(0, arg):
		if i < arg:
			i+=1

#partition that splits the array
def partition(array, low, high):
	i = (low-1)
	pivot = array[high] #pivot set as max

	for j in range(low, high):
		if(array[j] <= pivot):
			i = i+1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[high] = array[high], array[i+1]
	return (i+1)

#quicksort
def quicksort(array):
	n = len(array)
	quicksort.bestCase = n * log(n, 2)
	quicksort.worstCase = n*n
	quicksortActual(array, 0, len(array)-1)


def quicksortActual(array, low, high):
	if(low < high):
		pivot = partition(array, low, high)
		quicksortActual(array, low, pivot-1)
		quicksortActual(array, pivot+1, high)

#Mergesort
def mergesort(array):
	n = len(array)
	mergesort.bestCase = n * log(n, 2)
	mergesort.worstCase = n * log(n, 2)
	mergsortActual(array)

def mergsortActual(array):
	if(len(array) > 1):
		midpoint = len(array)/2
		left = array[:int(midpoint)]
		right = array[int(midpoint):]

		mergsortActual(left)
		mergsortActual(right)

		i = 0
		j = 0
		k = 0

		# Merge the arrays
		while(i < len(left) and j < len(right)):
			if(left[i] < right[j]):
				array[k] = left[i]
				i += 1
			else:
				array[k] = right[j]
				j += 1
			k += 1

		while(i < len(left)):
			array[k] = left[i]
			i += 1
			k += 1

		while(j < len(right)):
			array[k] = right[j]
			j += 1
			k += 1

#Heapsort
def max_heapify(array, heap_size, i):
	left, right = i*2+1, i*2+2
	largest = i
	if left < heap_size and array[left] > array[largest]:
		largest = left
	if right < heap_size and array[right] > array[largest]:
		largest = right
	if largest != i:
		array[i], array[largest] = array[largest], array[i]
		max_heapify(array, heap_size, largest)

def build_max_heap(array, size):
	for i in range(size // 2, -1, -1):
		max_heapify(array, size, i)

def heapsort(array):
	n = len(array)
	heapsort.bestCase = n * log(n, 2)
	heapsort.worstCase = n * log(n, 2)
	heapsortActual(array)

def heapsortActual(array):
	heap_size = len(array)
	build_max_heap(array, heap_size)
	while heap_size > 0:
		array[0], array[heap_size-1] = array[heap_size-1], array[0]
		heap_size -= 1
		max_heapify(array, heap_size, 0)
