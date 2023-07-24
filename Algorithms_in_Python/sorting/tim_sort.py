# Timsort

# Time complexity = O(nlogn)
# Space complexity = O(n)

"""
The Timsort
algorithm is an optimal algorithm for real-world long lists that is based on a combination of the merge sort and insertion sort algorithms.
The Timsort algorithm utilizes the best of both algorithms; insertion sort works best when the array is sorted partially and its size is small, 
and the merge method of the merge sort algorithm works fast when we have to combine small, sorted lists.

The main concept of the Timsort algorithm is that it uses the insertion sort algorithm to sort small blocks (also known as chunks) of data elements,
and then it uses the merge sort algorithm to merge all the sorted chunks. The main characteristic of the Timsort algorithm is that it takes advantage
of already-sorted data elements known as “natural runs,” which occur very frequently in real-world data.
"""

def Insertion_Sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        while search_index > 0 and unsorted_list[search_index-1] > insert_value :
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1
        unsorted_list[search_index] = insert_value
    return unsorted_list

def Merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list

def Tim_Sort(arr, run):
    for x in range(0, len(arr), run):
        arr[x : x + run] = Insertion_Sort(arr[x : x + run])
    
    runSize = run
    while runSize < len(arr):
        for x in range(0, len(arr), 2 * runSize):
            arr[x : x + 2 * runSize] = Merge(arr[x : x + runSize], arr[x +runSize: x + 2 * runSize])
        runSize = runSize * 2
