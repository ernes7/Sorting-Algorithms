import os
import errno
import sys
import random
import csv

# Generates a random list with unique values
# Max- range for sequence of numbers
# Size- the size of the list to return
# Max must be > than Size
def generate_random(max, size):
	return random.sample(range(max), size)

# Generates a random list with repeats
# Min- the lower bound
# Max- the upper bound inclusive
# Size- the size of the list
def generate_random_repeats(min, max, size):
	randomList = []
	for i in range(size):
		randomList.append(random.randint(min, max))
	return randomList

# Generates a sorted list
# Size - the size of the list
def generate_sorted(size):
	sortedList = []
	for i in range(size):
		sortedList.append(i)
	return sortedList

# Generates a reversed ordered list
# Size- the size of the list
def generate_reverse_sorted(size):
	reversedList = []
	for i in range(size, 0, -1):
		reversedList.append(i)
	return reversedList



#Initializes external datasets
#Example Use: 
#	$ python -c 'import utility; utility.initialize_datasets()'
def initialize_datasets():
	min = 0
	max = 100
	sizes = [100, 1000, 10000, 30000, 50000, 100000, 250000, 500000, 1000000]
	
	meta = [
		{
			"filename":"testValues/random.csv", 
			"func":generate_random_repeats, 
			"args": {"min": min, "max": max}
		},
		{
			"filename":"testValues/sorted.csv", 
			"func":generate_sorted, 
			"args": {}
		},
		{
			"filename":"testValues/reverse.csv", 
			"func":generate_reverse_sorted, 
			"args": {}
		},
	]

	for data in meta:
		generate_dataset(data["filename"], data["func"], data["args"], sizes)

#Generates datasets in an external file given the arguments.
#Arguments:
#	pathname (string) - The full path including filename
#	func (function)   - The function used to generate the dataset
#	args (dictionary) - A dictionary containing the arguments (expects: None, {min, max})
#	sizes (list)	  - A list of integer values representing the size of the datasets
#Example Usage:
#	$ python -c 'import utility; utility.generate_dataset("testValues/shortSorted.csv", utility.generate_sorted, {}, [1, 2, 3, 4, 5])'
def generate_dataset(pathname, func, args, sizes):
	if not os.path.exists(os.path.dirname(pathname)):
			try:
				os.makedirs(os.path.dirname(pathname))
			except OSError as e:
				if e.errno != errno.EEXIST:
					raise

	with open(pathname, "w") as f:
		file = csv.writer(f)
		for i in range(len(sizes)):
			if bool(args):
				file.writerow(func(args["min"], args["max"], sizes[i]))
			else:
				file.writerow(func(sizes[i]))

#Reads a csv file
#Returns an array where each entry is a subarray
def read_from_csv(filename):
	filename = "testValues/" + filename
	with open(filename,'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		data = []
		for line in csv_reader:
			if bool(line): #ignores empty lines
				subArray = []
				for number in line:
					subArray.append(int(number))
				data.append(subArray)

	return data
			
 # Takes arguments from the command line
 # returns the desired test values
def getValues(argc, argv):
	# biggest working value = int(sys.maxsize/100)
	default = int(sys.maxsize/100)
	testValues = []
	#"commandLine$ python test.py"
	if argc == 1:
		testValues = read_from_csv("large.csv")[8]
		#testValues = generate_random(default, default)

	# case of single int or filename
	#"commandLine$ python test.py 10000"
	#"commandLine$ python test.py testValues.csv"
	elif argc == 2:
		if argv[1].endswith(".csv"):
			testValues = read_from_csv(argv[1])
		elif argv[1].isdigit():
			testValues = generate_random(int(argv[1]), int(argv[1]))
		else:
			print("Error: Expected digit, found \"", argv[1], "\"")
			return []

	# case of two int params a and b.
	# a = the maximum range the numbers can be in
	# b = the number of elements in the list
	#"commandLine$ python test.py 10000 100"
	elif argc == 3:
		if argv[1].isdigit() and argv[2].isdigit():
			arg1 = int(argv[1])
			arg2 = int(argv[2])
			if arg1 >= arg2:
				testValues = generate_random(arg1, arg2)
			else:
				print("Error: Expected \"test.py a b\" where a >= b, a = max, b = size")
		else:
			print("Error: Expected digit, found \"",
				  argv[1], "\" and \"", argv[2], "\"")
			return []
	return testValues


def experimentalError(experimental, accepted):
	return int(abs(experimental - accepted)/accepted*100)
