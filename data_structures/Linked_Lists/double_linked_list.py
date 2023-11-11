class Node:
    """Implementation of the node"""
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    """Implementation of the double linked list"""
    def __init__ (self, head = None, tail = None, size = 0):
        self.head = head
        self.tail = tail
        self.size = size
        
    def __iter__(self):
        """Method to iterate the list"""
        while self.head:
            val = self.head.data
            current = self.head.next
            yield val

    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("The index must be an integer")
        
        if abs(index) > self.size or index == self.size:
            raise IndexError("Linked List index out of range") 
        
        count = 0
        
        if index == 0:
            return self.head.data
        elif index > 0:
            current = self.head
            while count != index:
                current = current.next 
                count += 1
            return current.data
        else:
            current = self.tail
            while count != index + 1:
                current = current.prev
                count -= 1 
            return current.data
        
    def __setitem__(self, index, data):
        new_node = Node(data)
        
        if not isinstance(index, int):
            raise TypeError("The index must be an integer")
        
        if abs(index) > self.size:
            raise IndexError("Linked List index out of range") 
        
        new_Node = Node(data)
        
        count = 0
        if index == 0:
            self.size -= 1
            self.push(data) 
        elif index == -1:
            self.size -= 1
            self.append(data)
        elif index > 0:
            current = self.head
            while count < index - 1:
                current = current.next
                count += 1 

            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
        else:
            current = self.tail
            while count != index + 1:
                current = current.prev
                count -= 1
            
            new_node.prev = current
            new_node.next = current.next
            current.next = new_node
            
        self.size += 1
                
        
    def append(self, data):
        """Method to append a node at the end to the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def push(self, data):
        """Method to insert a node at beginning to the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
            
            
    def popleft(self):
        """Method to delete the first node"""
        if self.head is None:
            raise IndexError("There is no node to delete")

        value = self.head
        self.head.prev = None
        self.head = self.head.next
        return value
    
    def pop(self):
        """Method to delete the last node"""
        if self.head is None:
            raise IndexError("There is no node to delete")
        
        value = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return value
        
    def delete(self, index):
        if not isinstance(index, int):
            raise TypeError("The index must be an integer")
        
        if abs(index) > self.size or index == self.size:
            raise IndexError("Linked List index out of range") 
        
        count = 0
        
        if index == 0 or index + self.size == 0:
            self.size += 1
            self.popleft()
        elif index in {self.size -1, -1}:
            self.size += 1
            self.pop()     
        elif index > 0:
            current = self.head
            while count != index:
                current = current.next 
                count += 1
            current.prev.next = current.next 
            current.next.prev = current.prev
        else:
            current = self.tail
            while count != index + 1:
                current = current.prev
                count -= 1 
            current.prev.next = current.next 
            current.next.prev = current.prev
        
        self.size -= 1

    def reverse(self):
        """Method to reverse the list"""
        prev = None

        while self.head:
            prev = self.head.prev
            self.head.prev = self.head.next
            self.head.next = prev
            self.head = self.head.prev
        self.head = prev.prev
    
    def clear(self):
        """Method to clear the list"""
        self.tail = None
        self.head = None

    def __repr__(self):
        """Method to print th list"""
        result = ""
        current = self.head
        while current:
            result = result + str(current.data) + " <-> "
            current= current.next
            
        return result + "end"

if __name__ == "__main__":
    doble_linked_list = DoublyLinkedList()
    doble_linked_list.append(5)
    doble_linked_list.push(15)
    doble_linked_list.push("a")
    print(doble_linked_list[-2])
    
    doble_linked_list[-1] = 2
    print(doble_linked_list)
    
    doble_linked_list.delete(-2)
    print(doble_linked_list)
    