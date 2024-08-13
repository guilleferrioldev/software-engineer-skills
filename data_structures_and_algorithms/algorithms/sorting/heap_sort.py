# Heap sort

# Time complexity = O(nlogn)
# Space complexity = O()

"""
Heap is an important data structure for sorting a list of elements since it is very suitable for a large number of elements. 
If we want to sort a list of elements, say in ascending order, we can use min-heap for this purpose; we first create a min-heap
of all the given data elements, and as per the heap property, the smallest data value will be stored at the root of the heap. 
With the help of the heap property, it is straightforward to sort the elements. The process is as follows:

- 1. Create a min-heap using all the given data elements.

- 2. Read and delete the root element, which is the minimum value. After that, copy the last element of the tree to the new root,
and further reorganize the tree to maintain the heap property.

- 3. Now, we repeat step 2 until we get all the elements.

- 4. Finally, we get the sorted list of elements
"""


class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
        self.root = 1

    #Helper method that takes care of arrangements of all the nodes after insertion of a new node
    def arrange(self, i):
        while i // 2 > 0:
            #compare the values between the parent and child node. If the parent is greater than the child, swap the two values
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            # after each iteration, move up in the tree
            i //= 2

    def insert(self, item):
        #insert an element using the append method
        self.heap.append(item)
        # increase the size of the heap
        self.size += 1
        # call the arrange() method to reorganize the heap (heapify it) to ensure that all the nodes in the heap satisfy the heap property
        self.arrange(self.size)

    
    # helper method for finding out which of the children to compare against the parent node.
    def minchild(self, k):
        #check if we get beyond the end of the list
        if k * 2 + 1 > self.size:
            # return the index of the left child
            return k * 2
        # Otherwise, we simply return the index of the lesser of the two children
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2 + 1

    # Method to reorganize the heap
    def sink(self, k):
        while k * 2 <= self.size:
            # we need to know which of the left or right children to compare against.
            mc = self.minchild(k)
            # compare parent and child to see whether we need to make the swap
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            # make sure that we move down the tree in each iteration
            k = mc

    # Method to delete the root node
    def delete_at_root(self):
        # copy the root element in a variable item
        item = self.heap[self.root]
        # the last element is moved to the root node
        self.heap[self.root] = self.heap[self.size]
        # reduce the size of the heap
        self.size -= 1
        # remove the element from the heap
        self.heap.pop()
        #  use the min_heapify() method to reorganize the heap element
        self.sink(self.root)
        return item

    # Method to sort the heap TC= O(nlogn)
    def heap_sort(self):
        sorted_list = []
        
        for node in range(self.size):
            n = self.delete_at_root()
            sorted_list.append(n)
        return sorted_list
    
    def print(self):
        print(self.heap[1:])
