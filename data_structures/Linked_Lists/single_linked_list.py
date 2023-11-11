### Single Linked List

# Implementation of the node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


# Implementation of the single linked list
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0
    
    #Function to iterate the linked list
    def iter(self):
        current = self.head
        
        while current:
            val = current.data
            current = current.next
            yield val

    #Function to insert an node at the end of the linked list 
    def append(self, data):
        node = Node(data)
        
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
    
    # Function to insert a node at the beginning of the linked list
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    #Function to insert  
    def insert_by_index(self, data, index):
        count = 0
        current = self.head
        node = Node(data)
        
        # Auxiliar counter to know what is the size of the list
        count_size = 0
        current_size = self.head
        while current_size:
            count_size += 1
            current_size = current_size.next
        
        if index == 0:
            node.next = self.head
            self.head = node

        elif index > count_size:
            print("Cannot insert, index is greater than the size of the list")

        else:
            while current:
                if count +1  == index:
                    node.next = current.next
                    current.next = node 
                    return 
                else:
                    count += 1 
                    current = current.next
    
    #Function to insert a node after an existing node
    def insert_by_element(self, data, new_node):
        current = self.head
        prev = self.head
        node = Node(new_node)

        while current:
            if current.data == data:
                node.next = current.next
                current.next = node
                return
            prev = current
            current = current.next
        else:
            print("Node does not exist")

    
    # Function to know if a node exists 
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    # Function to know the size of the list 
    def sizer(self):
        count = 0
        current = self.head
        
        while current:
            count += 1 
            current = current.next 

        return count

    # Function to delete the first element 
    def delete_first_node(self):
        current = self.head
        
        if self.head is None:
            print("There is no node to delete")
        elif current == self.head:
            self.head = current.next
    
    # Function to delete the last node 
    def delete_last_node(self):
        current = self.head
        prev = self.head
        
        while current:
            if current.next is None:
                prev.next = current.next
                self.size -= 1
            prev = current
            current = current.next
    
    # Function to delete a node at any position
    def delete(self, data):
        current = self.head
        prev = self.head

        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1      
                return
            prev = current
            current = current.next
    
    # Function to delete a node by its index 
    def delete_by_index(self, index):
        current = self.head
        prev = self.head
        count = 0
        
        # Auxiliar counter to know what is the size of the list
        count_size = 0
        current_size = self.head
        while current_size:
           count_size += 1
           current_size = current_size.next
        
        if index == 0:
            self.head = current.next

        elif index > count_size:
            print("Cannot delete, index is greater than the size of the list")
        
        else:
            while current:
                if count == index:
                    prev.next = current.next
                    return
                else:
                    count += 1
                    prev = current
                    current = current.next
        

    # Function to clear the list
    def clear(self):
        self.tail = None
        self.head = None
    
    # Function to reverse the list
    def reverse(self):
        prev = None
        
        while self.head is not None:
            self.head.next , prev, self.head = prev, self.head, self.head.next
        self.head = prev   
        

    # Function to print the list
    def print(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
