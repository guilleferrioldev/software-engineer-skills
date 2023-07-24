# Selection sort

# Time complexity = O(n²)
# Space complexity = O(1)

"""
The selection sort algorithm begins by finding the smallest element in the list and interchanges it with the data stored at the first position 
in the list. Thus, it sorts the sublist sorted up to the first element. This process is repeated for (n-1) times to sort n items.

Next, the second smallest element, which is the smallest element in the remaining list, is identified and interchanged with the second position 
in the list. This makes the initial two elements sorted. The process is repeated, and the smallest element remaining in the list is swapped with
the element in the third index on the list. This means that the first three elements are now sorted.
"""

def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)
    
    for i in range(size_of_list):
        small = i
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[small]:
                small = j
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[small]
        unsorted_list[small] = temp
