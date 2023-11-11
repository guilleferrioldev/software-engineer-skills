# Jump search

# Time Complexity = O(√n)
# Space Complexity = O(1)

"""
The jump search algorithm is an improvement over linear search for searching for a given element from an ordered (or sorted) list of elements. 
This uses the divide-and-conquer strategy in order to search for the required element. In linear search, we compare the search value with each 
element of the list, whereas in jump search, we compare the search value at different intervals in the list, which reduces the number of comparisons.

In this algorithm, firstly, we divide the sorted list of data into subsets of data elements called blocks. Within each block, the highest value 
will lie within the last element, as the array is sorted. Next, in this algorithm, we start comparing the search value with the last element of each block.

There can be three conditions:
- 1. If the search value is less than the last element of the block, we compare it with the next block.

- 2. If the search value is greater than the last element of the block, it means the desired search value must be present in the current block. 
So, we apply linear search in this block and return the index position.

- 3. If the search value is the same as the compared element of the block, we return the index position of the element and we return the candidate.
"""

import math

def search_ordered(ordered_list, term):
    ordered_list_size = len(ordered_list)
    
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i] > term:
            return -1
    return -1

def jump_search(ordered_list, item):
    list_size = len(ordered_list)
    block_size = int(math.sqrt(list_size))
    i = 0
    
    while i != len(ordered_list)-1 and ordered_list[i] <= item:
        if i+ block_size > len(ordered_list):
            block_size = len(ordered_list) - i
            block_list = ordered_list[i: i+block_size]
            j = search_ordered(block_list, item)
            if j == -1:
                print("Element not found")
                return
            return i + j
        if ordered_list[i + block_size -1] == item:
            return i+block_size-1
        elif ordered_list[i + block_size - 1] > item:
            block_array = ordered_list[i: i + block_size - 1]
            j = search_ordered(block_array, item)
            if j == -1:
                print("Element not found")
                return
            return i + j
        i += block_size
