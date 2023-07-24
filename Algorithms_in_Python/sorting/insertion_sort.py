# Insertion sort

# Time complexity = O(n²)
# Space complexity = O(1)

"""
The idea of insertion sort is that we maintain two sublists (a sublist is a part of the original larger list), one that is sorted and 
one that is not sorted, in which elements are added one by one from the unsorted sublist to the sorted sublist. So, we take elements 
from the unsorted sublist and insert them in the correct position in the sorted sublist, in such a way that this sublist remains sorted

In the insertion sort algorithm, we always start with one element, taking it to be sorted, and then take elements one by one from the
unsorted sublist and place them at the correct positions (in relation to the first element) in the sorted sublist. So, after taking one 
element from the unsorted sublist and adding it to the sorted sublist, now we have two elements in the sorted sublist. Then, we again take
another element from the unsorted sublist, and place it in the correct position (in relation to the two already sorted elements) in the
sorted sublist. We repeatedly follow this process to insert all the elements one by one from the unsorted sublist into the sorted sublist.
"""

def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        while search_index > 0 and unsorted_list[search_index-1] > insert_value :
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1
        unsorted_list[search_index] = insert_value
