# Sentinel Linear search

# Time complexity = O(n)
# Space complexity = O(1)

"""
In this search, the last element of the array is replaced with the element to be searched and then the linear search is performed on the array
without checking whether the current index is inside the index range of the array or not because the element to be searched will definitely be 
found inside the array even if it was not present in the original array since the last element got replaced with it. So, the index to be checked
will never be out of the bounds of the array.

Here are the steps for Sentinel Linear Search algorithm:
- 1. Initialize the search index variable i to 0.

- 2. Set the last element of the array to the search key.

- 3. While the search key is not equal to the current element of the array.

- 4.If i is less than the size of the array or arr[i] is equal to the search key, return the value of i (i.e., the index of the search key in the array).

- 5. Otherwise, the search key is not present in the array, so return -1
"""


def sentinel_search(lst, target):
    lst.append(target)
    i = 0
    while(lst[i] != target):
        i += 1
    if(i == len(lst)-1):
        return -1
    else:
        return i
