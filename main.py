import sys
import utility
import tests
import algorithms

def main():
	numInstr = int(sys.maxsize/100) #biggest working value = int(sys.maxsize/100)
	tickPerInstr = tests.compTime(algorithms.baseline, numInstr)/numInstr
	testValues = utility.getValues(len(sys.argv), sys.argv)
	algs = [
		algorithms.mergesort, 
		algorithms.heapsort, 
		algorithms.quicksort
	]

	if len(testValues) > 0:
		tests.runTests(tickPerInstr, algs, testValues)

if __name__ == "__main__":
	main()