# MinHeap implementation

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


   # helper function to swap the two given nodes of the heap
    def swapnodes(self, node1, node2):
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]
  
    # THE MIN_HEAPIFY FUNCTION
    def min_heapify(self, i):
  
        # If the node is a not a leaf node and is greater than any of its child
        if not (i >= (self.size//2) and i <= self.size):
            if (self.heap[i] > self.heap[2 * i]  or  self.heap[i] > self.heap[(2 * i) + 1]): 
                if self.heap[2 * i] < self.heap[(2 * i) + 1]:
        # Swap the node with the left child and then call the min_heapify function on it
                    self.swapnodes(i, 2 * i)
                    self.min_heapify(2 * i)
  
                else:
                # Swap the node with right child and then call the min_heapify function on it
                    self.swapnodes(i, (2 * i) + 1)
                    self.min_heapify((2 * i) + 1)
    
    
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

    # Method to delete a node at any location
    def delete(self, location):
        item = self.heap[location + 1]
        self.heap[location + 1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.min_heapify(location + 1)
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

# Test
"""
h = MinHeap()
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
for i in unsorted_list:
    h.insert(i)

h.print()
h.delete(3)
print(h.heap_sort())
print()
"""