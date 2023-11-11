### Stacks

# Stacks implemnetation using Array-based

class Stack_Arrays:
    def __init__(self, size):
        self.items = []
        self.top = -1
        self.size = size
    
    # Function to know if a stack is empty
    def isEmpty(self):
        return self.items == []
    
    # Function to add an element 
    def push(self, item):
        if self.top >= self.size -1 :
            print("Stack Overflow")
        else:    
            self.top += 1
            self.items.append(item)
    

    # Function to delete an element 
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            self.top -= 1
            return self.items.pop()
    

    # Function to check the top element
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            return self.items[self.top]

    # Function to print the stack
    def print(self):
        print(self.items)




# Stack implementation using single linked lists 

# Node implementation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack_List:
    def __init__(self):
        self.top = None
        self.size = 0

    #  Function to know if the stack is empty
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    # Function to add an element 
    def push(self, data):
        # create a new node
        node = Node(data)
    
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1
    

    # Function to delete an element 
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next: #check if there is more than one node.
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print("Stack is empty")

    
    # Function to check the top element
    def peek(self):
        if self.top:
            return self.top.data    
        else:   
            print("Stack is empty")

    # Function to print the stack
    def print(self):
        current = self.top
        while current:
            print(current.data, end = " -> ")
            current = current.next
