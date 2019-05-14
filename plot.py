
##### FOR MAC USERS #####
# brew install python ( needs homebrew )
# pip install matplotlib --user
# pip install python-tk
# install anaconda ( I dont think this is needed)
# VScode extension -> code runner
################################
import matplotlib.pyplot as plt
import utility
import algorithms
import tests
random = utility.read_from_csv("random.csv")

times_merge = [
    tests.compTime(algorithms.mergesort, random[0]), 
    tests.compTime(algorithms.mergesort, random[1]), 
    tests.compTime(algorithms.mergesort, random[2]), 
    tests.compTime(algorithms.mergesort, random[3]), 
    tests.compTime(algorithms.mergesort, random[4]), 
    tests.compTime(algorithms.mergesort, random[5])
] # replace it with input

random = utility.read_from_csv("random.csv")
times_quick = [
    tests.compTime(algorithms.quicksort, random[0]), 
    tests.compTime(algorithms.quicksort, random[1]), 
    tests.compTime(algorithms.quicksort, random[2]), 
    tests.compTime(algorithms.quicksort, random[3]), 
    tests.compTime(algorithms.quicksort, random[4]), 
    tests.compTime(algorithms.quicksort, random[5])
] #  replace it with input

random = utility.read_from_csv("random.csv")
times_heapsort = [
    tests.compTime(algorithms.heapsort, random[0]), 
    tests.compTime(algorithms.heapsort, random[1]), 
    tests.compTime(algorithms.heapsort, random[2]), 
    tests.compTime(algorithms.heapsort, random[3]), 
    tests.compTime(algorithms.heapsort, random[4]), 
    tests.compTime(algorithms.heapsort, random[5])
] # replace it with input

## Function takes 3 arrays of times from the algorithms ##
## Arrays are size 5. Corresponding to input size in line 25 ##
## Function 4th parameter takes name of input type ##
## Function plots the times into a Line Chart ##
## X -> Input Size     Y -> Alg Times ##

type_input = 'Random/Sorted/Unsorted Input Size' # test for input size argument

def plot(times_merge, times_quick, times_heapsort, type_input):
    

    size = [10, 100, 1000, 10000,100000, 1000000]
    
    plt.plot(size, times_merge, color='g',label='MergeSort')
    plt.plot(size, times_quick, color='b',label='QuickSort')
    plt.plot(size, times_heapsort, color='r',label='HeapSort')
    plt.legend(loc='upper left')
    plt.xlabel('Input Size')
    plt.ylabel('Times in Seconds')
    plt.title(type_input) # random OR sorted OR unsorted
    plt.autoscale(enable=True, axis='both',tight=None)

    plt.show()

plot(times_merge,times_quick,times_heapsort,type_input)