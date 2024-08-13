# Expoential search

# Time complexity = O(logn)
# Space complexity = O(logn)

"""
Exponential search is another search algorithm that is mostly used when we have large numbers of elements in a list. Exponential search 
is also known as galloping search and doubling search. The exponential search algorithm works in the following two steps:
- 1. Given a sorted array of n data elements, we first determine the subrange in the original list where the desired search item may be present 

- 2. Next, we use the binary search algorithm to find out the search value within the subrange of data elements identified in step 1

Firstly, in order to find out the subrange of data elements, we start searching for the desired item in the given sorted array by jumping 
2**i elements every iteration. Here, i is the value of the index of the array. After each jump, we check if the search item is present between
the last jump and the current jump. If the search item is present then we use the binary search algorithm within this subarray, and if it is 
not present, we move the index to the next location. Therefore, we first find the first occurrence of an exponent i such that the value at index
2**i is greater than the search value. Then, the 2**i becomes the lower bound and 2**i-1 becomes the upper bound for this range of data elements 
in which the search value will be present. The exponential search algorithm is defined as follows:

- 1. First, we check the first element A[0] with the search element.

- 2. Initialize the index position i=1.

- 3. We check two conditions: (1) if it is the end of the array or not (i.e. 2i < len(A)), and (2) if A[i] <= search_value). In the first condition,
we check if we have searched the complete list, and we stop if we have reached the end of the list. In the second condition, we stop searching when
we reach an element whose value is greater than the search value, because it means the desired element will be present before this index position (since the list is sorted).

- 4. If either of the above two conditions is true, we move to the next index position by incrementing i in powers of 2.

- 5. We stop when either of the two conditions of step 3 is satisfied.

- 6. We apply the binary search algorithm on the range 2**i//2 to min (2**i , len(A))
"""

def binary_search_recursive(ordered_list, first_element_index, last_element_index, term):
    if (last_element_index < first_element_index):
        return None
    else:
        mid_point = first_element_index + ((last_element_index - first_element_index) // 2)
        if ordered_list[mid_point] > term:
            return binary_search_recursive (ordered_list, first_element_index, mid_point-1, term)
        elif ordered_list[mid_point] < term:
            return binary_search_recursive (ordered_list, mid_point+1,last_element_index, term)
        else:
            return mid_point

def exponential_search(array, search_value):
    if (array[0] == search_value):
        return 0
    index = 1
    while index < len(array) and array[index] < search_value:
        index *= 2
    return binary_search_recursive(array, index // 2, min(index, len(array) - 1), search_value)
