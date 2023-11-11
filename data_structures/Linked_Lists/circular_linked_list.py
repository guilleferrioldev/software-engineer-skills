### Circular Linked List

# Implementation of the node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


# Implementation of the circular linked list
class CircularList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0

    # Function to insert a node at the end of the list
    def append(self, data):
        # Create a new node
        node = Node(data)
        

        if self.tail:
            self.tail.next = node
            self.tail = node
            node.next = self.head
        else:
            self.head = node
            self.tail = node
            self.tail.next = self.tail
            self.size += 1
    
    # Function to insert a node at the beginning of the list
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.tail.next = node
        self.size += 1

    # Function to iterate through the list
    def iter(self):
        current = self.head
        
        while current:
            val = current.data
            current = current.next
            yield val
    
    # Function to know if a node exists
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False
    
    # Function to delete a node in the list
    def delete(self, data):
        current = self.head
        prev = self.head
        
        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    #item to be deleted is head node
                    self.head = current.next
                    self.tail.next = self.head
                elif current == self.tail:
                    #item to be deleted is tail node
                    self.tail = prev
                    prev.next = self.head
                else:
                    #item to be deleted is an intermediate node
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
    
    # Function to clear the list 
    def clear(self):
        self.tail = None
        self.head = None
    
    # Function to print the list
    def print(self, number):
        counter = 1
        for word in words.iter():
            print(word, end = " -> ")
            counter += 1
            if counter > number:
                break
