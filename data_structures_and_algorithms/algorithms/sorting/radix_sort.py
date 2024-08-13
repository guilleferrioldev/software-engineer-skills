# Radix sort 

# Time complexity = O(nk)
# Space complexity = O(n + k)

"""
Radix sort is a sorting algorithm that sorts the elements by first grouping the individual digits of the same place value. Then, sort the 
elements according to their increasing/decreasing order.

- 1. Find the largest element in the array

- 2. Now, go through each significant place one by one.Use any stable sorting technique to sort the digits at each significant place. 
We have used counting sort for this.
"""

# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
