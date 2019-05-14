import time
import utility
import sys
from copy import deepcopy
sys.setrecursionlimit(50000)

#Test function manager
#Recursively runs tests on each algorithm passed
#Takes:
#	tpi  (int)         - Ticks per instruction
#	algo (list(func))  - The algorithm(s) to test
#	arg	 (array)       - The array of test values
#Returns:
#	Void
def runTests(tpi, algos, arg):
	if len(algos) > 0:
		print(algos[0].__name__)
		print("n =", len(arg))
		printTimeTest(tpi, algos[0], arg)
		printSortTest(algos[0], arg)
		print("")
		runTests(tpi, algos[1:], arg)

#Returns measured time in CPU ticks of some f(x)
#Takes:
#	f (func) - The function to measure
#	x (*)    - Argument(s) to the function
#Returns:
#	(int) - Total time in CPU clock ticks for the function to complete
def compTime(f, x):
	start = time.perf_counter()
	f(x)
	end = time.perf_counter()
	return end - start

#Prints timing information
#Takes:
#	tpi  (int)   - Ticks per instruction
#	algo (func)  - The algorithm to test
#	arg	 (array) - The array of test values
#Returns:
#	Void
def printTimeTest(tpi, algo, arg):
	measuredTicks = compTime(algo, deepcopy(arg))
	expectedBest = algo.bestCase*tpi
	expectedBest = algo.worstCase*tpi
	print("Predicted best case.:", algo.bestCase*tpi)
	print("Predicted worst case:", algo.worstCase*tpi)
	print("Measured ticks......:", measuredTicks)

#Prints sorting information
#Takes:
#	algo (func)  - The algorithm to test
#	arg	 (array) - The array of test values
#Returns:
#	Void
def printSortTest(algo, arg):
	cpy = deepcopy(arg)
	algo(cpy)
	print("List changed? ", cpy != arg)
	print("List sorted? ", cpy == sorted(arg))
