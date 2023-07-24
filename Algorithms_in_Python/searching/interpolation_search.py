# Interpolation search

# Time complexity = O(loglogn)
# Space complexity = O(1)

"""
The interpolation search algorithm works efficiently when there are uniformly distributed elements in the sorted list. In a binary search,
we always start searching from the middle of the list, whereas in the interpolation search we compute the starting search position depending 
on the item to be searched. In the interpolation search algorithm, the starting search position is most likely to be close to the start or end 
of the list; if the search item is near the first element in the list, then the starting search position is likely to be near the start of the 
list and if the search item is near the end of the list, then the starting search position is likely to be near the end of the list.

The interpolation search algorithm works as follows:

- 1. We start searching for the given search value from the midpoint (we have just seen how to compute it).

- 2. If the search value matches the value stored at the index of the midpoint, we return this index position.

- 3. If the search value does not match the value stored at the midpoint, we divide the list into two sublists, i.e. a higher sublist and lower sublist.
The higher sublist has all the elements with higher index values than the midpoint, and the lower sublist has all the elements with lower index values.

- 4. If the search value is greater than the value of the midpoint, we search the given search value in the higher sublist and ignore the lower sublist.

- 5. If the search value is lower than the value of the midpoint, we search the given search value in the lower sublist and ignore the higher sublist.

- 6. We repeat the process until the size of the sublists is reduced to zero.
"""

def nearest_mid(input_list, low_index, upper_index, search_value):
    mid = low_index + (( upper_index - low_index)/(input_list[upper_index] - input_list[low_index])) * (search_value - input_list[low_index])
    return int(mid)

def interpolation_search(ordered_list, search_value):
    low_index = 0
    upper_index = len(ordered_list) -1

    while low_index <= upper_index:
        mid_point = nearest_mid(ordered_list, low_index, upper_index,search_value)
        if mid_point > upper_index or mid_point < low_index:
            return None
        if ordered_list[mid_point] == search_value:
            return mid_point
        if search_value > ordered_list[mid_point]:
            low_index = mid_point + 1
        else:
            upper_index = mid_point -1
    if low_index > upper_index:
        return None
