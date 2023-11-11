### Double Linked List

# Implementation of the node 
class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

# Implementation of the double linked list
class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.count = 0


    #Function to append a node at the end to the list
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1


    #Function to insert a node at beginning to the list.
    def push(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    
    # Function to insert a node after an existing node
    def insert_by_element(self, data, new_node):
        current = self.head
        prev = self.head
        new_node = Node(new_node, None, None)

        while current:
            if current.data == data:
                new_node.prev = current
                new_node.next = current.next
                current.next = new_node
                self.count += 1
            prev = current
            current = current.next
    

    # Function to insert a node in an index
    def insert_by_index(self, data ,index):
        count = 0
        current = self.head
        prev = self.head
        new_node = Node(data, None, None)
        
        # Size of the list
        count_sizer = 0
        current_2 = self.head
        while current_2:
            count_sizer += 1 
            current_2 = current_2.next
        
        # Insert item in the first node 
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = self.head
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.count += 1
            
        # Insert item in the last node
        elif index == count_sizer:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        # When index is greater than the size of the list
        elif index > count_sizer:
            print("Cannot insert, index is greater than the size of the list")
        
        # Insert node at the middle of the list
        else:
            while current:
                if count == index:
                    new_node.prev = prev
                    new_node.next = current
                    prev.next = new_node
                    current.prev = new_node
                    self.count += 1
                    return
                count += 1
                prev = current
                current = current.next
                            
    
    # Function to iterate the list
    def iter(self):
        while self.head:
            val = self.head.data
            current = self.head.next
            yield val
    
    # Functionto know the size of the list
    def sizer(self):
        count= 0

        while self.head:
            count += 1 
            self.head = self.head.next 
        return count


    # Function to kow if a node exists
    def search(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True 
        return False 

    
    # Function to delete a node by name
    def delete(self, data):
        # Delete a node from the list.
        current = self.head
        node_deleted = False

        if current is None:
        #List is empty
            print("List is empty")
        elif current.data == data:
            #Item to be deleted is found at beginning of the list
            self.head.prev = None
            node_deleted = True
            self.head = current.next
        elif self.tail.data == data:
            #Item to be deleted is found at the end of list
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
            #search item to be deleted, and delete that node
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
            if node_deleted == False:
                # Item to be deleted is not found in the list
                print("Cannot delete, item not found")
        if node_deleted:
            self.count -= 1
    
    
    #  Function to delete a node at any position
    def delete_by_index(self, index):
        count = 0
        current = self.head
        prev = self.head
        node_deleted = False
        
        # Size of the list
        count_sizer = 0
        current_2 = self.head
        while current_2:
            count_sizer += 1
            current_2  = current_2.next
        
        # Item to be deleted is found at the starting of the list
        if index == 0:
            self.head.prev = None
            node_deleted = True
            self.head = current.next
        
        # Item to be deleted is found at the end of the list
        elif index == count_sizer -1:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                # Search item to be deleted, and delete the node
                if count == index:
                    current.prev.next = current.next
                    current.next.prev = prev
                    node_deleted = True
                    return 
                else:    
                    count += 1
                    prev = current
                    current = current.next

            if node_deleted == False:
                #Item to be deleted is not found in the list
                print("Cannot delete, index not found")
        if node_deleted:
            self.count -= 1
                
    
    # Function to delete the first node
    def delete_first_node(self):
        """
        Check if there is no item to delete from the list, and we print the appropriate message.
        """
        if self.head is None:
            print("There is no node to delete")
        else:
            self.head.prev = None
            self.head = current.next
    
    # Function to delete the last node
    def delete_last_node(self):
        if self.head is None:
            print("There is no node to delete")
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # Function to reverse the list
    def reverse(self):
        prev = None

        while self.head:
            prev = self.head.prev
            self.head.prev = self.head.next
            self.head.next = prev
            self.head = self.head.prev
    self.head = prev.prev
    
    # Function to clear the list
    def clear(self):
        self.tail = None
        self.head = None

    # Function to print th list
    def print(self):
        while self.head:
            print(self.head.data, end = " <-> ")
            self.head = self.head.next
