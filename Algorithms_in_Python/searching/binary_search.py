# Binary Search 

"""
The binary search algorithm works as follows. It starts searching for the item by dividing the given list in half. If the search
item is smaller than the middle value then it will look for the searched item only in the first half of the list, and if the search
item is greater than the middle value it will only look at the second half of the list. We repeat the same process every time until
we find the search item, or we have checked the whole list. In the case of a non-numeric list of data items, for example, if we have
string data items, then we should sort the data items in alphabetical order (similar to how a contact list is stored on a phone)
"""


# Binary search iterative

# Time complexity = O(logn)
# Space complexity = O(1)

def binary_search_iterative(ordered_list, term):
    index_of_first_element = 0
    index_of_last_element = len(ordered_list)-1
    
    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point -1
    if index_of_first_element > index_of_last_element:
        return None

# Binary search recursive

# Time complexity = O(logn)
# Space complexity = O(logn)

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
