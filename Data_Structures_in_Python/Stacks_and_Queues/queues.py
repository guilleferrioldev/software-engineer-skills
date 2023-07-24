### Queues

# Implementation using Arrays
class Queue_Array:
    def __init__(self, size = None):
        self.items = []
        self.front = self.rear = 0
        self.size = size
    
    # Function to enqueue an element
    def enqueue(self, data):
        if self.size == self.rear:
            print("Queue is full")
        else:
            self.items.append(data)
            self.rear += 1
    
    # Function to dequeue an element
    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            data = self.items.pop(0) #delete the item from front end of the queue
            self.rear -= 1
            return data
    
    # Function to print the queue
    def print(self):
        print(self.items)



# Implementation using linked lists

# Implementation of the node
class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    # Function to eneque an element
    def enqueue(self, data):
        new_node = Node(data, None, None)
        
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1

    # Function to dequeue an element
    def dequeue(self):
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
        elif self.count <1:
            print("Queue is empty")
        
        self.count -= 1 

    # Function to print the queue
    def print(self):
        current = self.head
        while current:
            print(current.data, end = " <-> ")
            current = current.next



# Implementation using stack

class Queue_Stack:
    def __init__(self):
        self.Stack1 = []
        self.Stack2 = []
    
    # Function to enqueue an element
    def enqueue(self, data):
        self.Stack1.append(data)
    
    # Function to dequeue an element
    def dequeue(self):
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
        if not self.Stack2:
            print("No element to dequeue")
            return
        return self.Stack2.pop()
    
    # Function to print the stack1
    def print_stack1(self):
        print(self.Stack1)
    
    # Function to print the stack2
    def print_stack2(self):
        print(self.Stack2)
