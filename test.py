import random
import time
import sys
from copy import deepcopy
from timeit import default_timer as timer
import utility
sys.setrecursionlimit(50000)

#Parition
def partition(array, low, high):
	i = (low-1)
	pivot = array[high]

	for j in range(low, high):
		if(array[j] <= pivot):
			i = i+1
			array[i], array[j] = array[j], array[i]
	array[i+1], array[high] = array[high], array[i+1]
	return (i+1)

#quicksort
def quicksort(array):
	quicksortActual(array, 0, len(array)-1)

def quicksortActual(array, low, high):
	if(low < high):
		pivot = partition(array, low, high)
		quicksortActual(array, low, pivot-1)
		quicksortActual(array, pivot+1, high)

#Mergesort
def mergesort(array):
	if(len(array) > 1):
		midpoint = len(array)/2
		left = array[:int(midpoint)]
		right = array[int(midpoint):]

		mergesort(left)
		mergesort(right)

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
	heap_size = len(array)
	build_max_heap(array, heap_size)
	while heap_size > 0:
		array[0], array[heap_size-1] = array[heap_size-1], array[0]
		heap_size -= 1
		max_heapify(array, heap_size, 0)

#timing function
def mapTests(algos, arg):
	if len(algos) > 0:
		print(algos[0].__name__, "tested with", len(arg), "elements")
		printTimeTest(algos[0], deepcopy(arg))
		printSortTest(algos[0], deepcopy(arg))
		print("\n")
		mapTests(algos[1:], arg)

def timeTest(algo, arg):
	start = time.process_time()
	algo(arg)
	end = time.process_time()
	return end - start

def printTimeTest(algo, arg):
	test = timeTest(algo, arg)
	print("Completed in: ", test, " ticks")
	#print("Expected time complexity (unconverted):", algo.complexity)# @todo: need to convert
	#print("T(n)/complexity: ", test/algo.complexity)

def printSortTest(algo, arg):
	orig = deepcopy(arg)
	algo(arg)
	print("List changed? ", orig != arg)
	print("List sorted? ", sorted(arg) == arg)

def getInput(argc, argv):
	default = int(sys.maxsize/100) #biggest working value = int(sys.maxsize/100)
	testValues = []

	#default case of no arguments
	if argc == 1:
		testValues = utility.generate_random(default, default)

	#case of single int or filename
	elif argc == 2:
		if argv[1].endswith(".csv"):
			n = 0 #unimplemented: need to read in param from file?
		elif argv[1].isdigit():
			testValues = utility.generate_random(int(argv[1]), int(argv[1]))
		else:
			print("Error: Expected digit, found \"", argv[1], "\"")
			return []

	#case of two int params
	elif argc == 3:
		if argv[1].isdigit() and argv[2].isdigit():
			arg1 = int(argv[1])
			arg2 = int(argv[2])
			if arg1 >= arg2:
				testValues = utility.generate_random(arg1, arg2)
			else:
				print("Error: Expected \"test.py a b\" where a >= b, a = max, b = size")
		else:
			print("Error: Expected digit, found \"", argv[1], "\" and \"", argv[2], "\"")
			return []
	return testValues

def main():
	testValues = getInput(len(sys.argv), sys.argv)
	algorithms = [heapsort, quicksort, mergesort]


	if len(testValues) > 0:
		mapTests(algorithms, testValues)


if __name__ == "__main__":
	main()
