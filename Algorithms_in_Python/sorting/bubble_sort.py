# Bubble sort

# Time complexity = O(n²)
# Space complexity = O(1)

"""
The idea behind the bubble sort algorithm is very simple. Given an unordered list, we compare adjacent elements in the list, and after each 
comparison, we place them in the right order according to their values. So, we swap the adjacent items if they are not in the correct order.
This process is repeated n-1 times for a list of n items.

In each iteration, the largest element of the list is moved to the end of the list. After the second iteration, the second largest element
will be placed at the second-to-last position in the list. The same process is repeated until the list is sorted.
"""


def bubble_sort(unordered_list):
    iteration_number = len(unordered_list)-1
    
    for i in range(iteration_number,0,-1):
        for j in range(i):
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
