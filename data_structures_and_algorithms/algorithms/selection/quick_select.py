# Quickselect

# Time complexity = O(n)
# Space complexity = O(1)

"""
The quickselect algorithm is used to obtain the k**th smallest element in an unordered list of items. It is based on the quicksort algorithm, 
in which we recursively sort the elements of both the sublists from the pivot point. In each iteration, the pivot value reaches the correct position 
in the list, which divides the list into two unordered sublists (left and right sublists), where the left sublist has smaller values as compared to
the pivot value, and the right sublist has greater values compared to the pivot value. Now, in the case of the quickselect algorithm, we recursively 
call the function only for the sublist that has the k**th smallest element.


In the quickselect algorithm, we compare the index of the pivot point with the k value to obtain the k**th smallest element from the given unordered list. 
There will be three cases in the quickselect algorithm, as follows:
- 1. If the index of the pivot point is smaller than k, then we are sure that the k**th smallest value will be present on the right-hand sublist of the pivot 
point. So we only recursively call the quickselect function for the right sublist.

- 2. If the index of the pivot point is greater than k, then it is obvious that the kth smallest element will be present on the left-hand side of the pivot 
point. So we only recursively look for the i**th element in the left sublist

- 3. If the index of the pivot point is equal to k, then it means that we have found out the k**th smallest value, and we return it.
"""

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [item for item in array[1:] if item <= pivot]
        greater = [item for item in array[1:] if item > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

def kth_element(array, target):
    return quick_sort(array)[target - 1]
