# Quicksort

# Time complexity = O(nlogn)
# Space complexity = O(logn)

"""
Quicksort is an efficient sorting algorithm. The quicksort algorithm is based on the divide-and-conquer class of algorithms, similar to the
merge sort algorithm, where we break (divide) a problem into smaller chunks that are much simpler to solve, and further, the final results
are obtained by combining the outputs of smaller problems (conquer)

The concept behind quicksorting is partitioning a given list or array. To partition the list, we first select a data element from the given list,
which is called a pivot element.

We can choose any element as a pivot element in the list. However, for the sake of simplicity, we’ll take the first element in the array as the
pivot element. Next, all the elements in the list are compared with this pivot element. At the end of first iteration, all the elements of the list 
are arranged in such a way that the elements which are less than the pivot element are arranged to the left of the pivot, that the elements that are
greater than the pivot element are arranged to the right of the pivot.
"""

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [item for item in array[1:] if item <= pivot]
        greater = [item for item in array[1:] if item > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)
