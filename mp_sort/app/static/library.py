from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)  # Set the seed for reproducibility
	return [random.randint(0, 9) for _ in range(number)]  # Generate 'number' random integers between 0 and 9

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	array = gen_random_int(number, seed)
	
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = ', '.join(map(str, array)) + '.'

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	pass

	array_str = None
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	# Step 1: Split the string into a list of numbers
	try:
		numbers = [int(num.strip()) for num in value.split(',')]
	except ValueError:
		window.alert("Please enter valid numbers separated by commas.")
		return

	# Step 2: Sort the list of numbers using Heap Sort
	heap_sort(numbers)

	# Step 3: Convert the sorted list back into a comma-separated string
	array_str = ','.join(map(str, numbers))

	# Step 4: Display the result in the <div id="sorted">
	document.getElementById("sorted").innerHTML = array_str

# Heapify function to maintain the max-heap property
def heapify(arr, n, i):
	largest = i  # Initialize largest as root
	left = 2 * i + 1  # Left child
	right = 2 * i + 2  # Right child

	# Check if left child exists and is greater than the root
	if left < n and arr[left] > arr[largest]:
		largest = left

	# Check if right child exists and is greater than the current largest
	if right < n and arr[right] > arr[largest]:
		largest = right

	# If largest is not the root
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # Swap

		# Heapify the affected sub-tree
		heapify(arr, n, largest)


# Heap Sort function
def heap_sort(arr):
	n = len(arr)

	# Build a maxheap (rearrange the array)
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one, extract elements
	for i in range(n - 1, 0, -1):
		# Swap the root (largest value) with the last element
		arr[i], arr[0] = arr[0], arr[i]

		# Heapify the root element to maintain the max-heap property
		heapify(arr, i, 0)

