#implementationusing list of tuples

# class for Node with data and priority
class Node:
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority

# class for Priority queue
class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Method to insert elements 
    def insert(self, node):
        # cheack if there is no elements
        if len(self.queue) == 0:
            # add the new node
            self.queue.append(node)
        else:
            # traverse the queue to find the right place for new node
            for x in range(0, len(self.queue)):
                # if the priority of new node is greater
                if node.priority >= self.queue[x].priority:
                    # if we have traversed the complete queue
                    if x == (len(self.queue)-1):
                        # add new node at the end
                        self.queue.insert(x+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True
    
    # Method to delete elements
    def delete(self):
        # remove the first node from the queue
        x = self.queue.pop(0)
        print("Deleted data with the given priority-", x.info, x.priority)
        return x

    
    # Print the priority queue
    def print(self):
        for x in self.queue:
            print(str(x.info)+ " - "+ str(x.priority))

"""
# Test
p = PriorityQueue()
p.insert(Node("Cat", 13))
p.insert(Node("Bat", 2))
p.insert(Node("Rat", 1))
p.insert(Node("Ant", 26))
p.insert(Node("Lion", 25))
p.print()
p.delete()
"""

class PriorityQueueHeap:
    def __init__(self):
        self.heap = [()]
        self.size = 0
    
    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k][0] < self.heap[k//2][0]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self,priority, item):
        self.heap.append((priority, item))
        self.size += 1
        self.arrange(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k][0] > self.heap[mc][0]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc
    
    def minchild(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2][0] < self.heap[k*2+1][0]:
            return k * 2
        else:
            return k * 2 + 1
    
    def delete_at_root(self):
        item = self.heap[1][1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

"""
# Test
h = PriorityQueueHeap()
h.insert(2, "Bat")
h.insert(13,"Cat")
h.insert(18, "Rat")
h.insert(26, "Ant")
h.insert(3, "Lion")
h.insert(4, "Bear")

for i in range(h.size):
    n = h.delete_at_root()
    print(n)
    print(h.heap)
"""
