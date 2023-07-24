# Counting sort 

# Time complexity = O(n+k)
# Space complexity = O(k)

"""
Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the 
array. The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.

- 1. Find out the maximum (let it be max)element from the given array

- 2. Initialize an array of length max+1 with all elements 0. This array is used for storing the count of the elements in the array. 

- 3. Store the count of each element at their respective index in count array
 
- 4. Store cumulative sum of the elements of the count array. It helps in placing the elements into the correct index of the sorted array

- 5. Find the index of each element of the original array in the count array. This gives the cumulative count. Place the element at the index 
calculated as shown in figure below. 
"""


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]
