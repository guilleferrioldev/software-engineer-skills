### Circular Linked List

from typing import Self, Any

class Node:
    """Implementation of the node"""
    def __init__(self, data = None):
        self.data = data
        self.next = None

class CircularLinkedList:
    """Implementation of the circular linked list"""
    def __init__ (self, tail = None, head = None, size = 0):
        self.tail = tail
        self.head = head
        self.size = size
        
    def __iter__(self):
        """Method to iterate through the list"""
        current = self.head
        
        while current:
            value = current.data
            current = current.next
            yield value
            
    def __len__(self):
        return self.size

    def append(self, data):
        """Method to insert a node at the end of the list"""
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
        
    
    def push(self, data):
        """Method to insert a node at the beginning of the list"""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.tail.next = node
        self.size += 1

    def delete(self, data):
        """Method to delete a node in the list"""
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
    
    def clear(self) -> None:
        """Method to clear the list"""
        self.tail = None
        self.head = None

    def __repr__(self) -> str:
        """Method to print the list"""
        return self.__getitem__(len(self))
    
    def __getitem__(self, number: int) -> str:
        """Auxiliar method to print the list"""
        counter = 1
        result = ""
        for word in self:
            result = result + str(word) + " -> "
            counter += 1
            if counter > number:
                break
            
        return result + "end"
    
if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list_2 = CircularLinkedList()
    circular_linked_list.append(5)
    circular_linked_list.push(10)
    
    print(circular_linked_list)
    print(circular_linked_list[5])
    
    circular_linked_list.delete(10)
    print(circular_linked_list)

    
