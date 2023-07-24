# MaxHeap implementation

class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
        self.root = 1

    #Helper method that takes care of arrangements of all the nodes after insertion of a new node
    def arrange(self, i):
        while i // 2 > 0:
            #compare the values between the parent and child node. If the parent is greater than the child, swap the two values
            if self.heap[i] > self.heap[i//2]:
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
    # in order to swap nodes which are not in order (not satisfy max-heap property)
    def swapnodes(self, node1, node2):
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]
  
    # THE MAX_HEAPIFY FUNCTION
    def max_heapify(self, i):
  
        # If the node is a not a leaf node and is lesser than any of its child
        if not (i >= (self.size//2) and i <= self.size):
            if (self.heap[i] < self.heap[2 * i]  or  self.heap[i] < self.heap[(2 * i) + 1]): 
                if self.heap[2 * i] > self.heap[(2 * i) + 1]:
     # Swap the node with the left child and call the max_heapify function on it
                    self.swapnodes(i, 2 * i)
                    self.max_heapify(2 * i)
  
                else:
                # Swap the node with right child and then call the max_heapify function on it
                    self.swapnodes(i, (2 * i) + 1)
                    self.max_heapify((2 * i) + 1)



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
        #  use the max_heapify() method to reorganize the heap element
        self.max_heapify(self.root)
        return item

    # Method to delete a node at any location
    def delete(self, location):
        item = self.heap[location + 1]
        self.heap[location + 1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.max_heapify(location +1)
        return item
    

    def print(self):
        print(self.heap[1:])
