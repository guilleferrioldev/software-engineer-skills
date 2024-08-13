# Deque implementation using Linked List

from typing import Any, List, Self, Iterable

class Node:
    """Implementation of the node"""
    def __init__(self, data: Any = None, next: Self = None, prev: Self = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Deque:
    """Implementation using Linked List"""
    def __init__(self, items: List[Any] = None) -> None:
        if items is not None:
            self.__create_items(items)
        else:
            self.__create_items([])
        
    def __create_items(self, items: List[Any]) -> None:
        """Method to insert the elements when a list is introduced when the class is instantiated"""
        if len(items) == 0:
            self.head = None
            self.tail = None
            self.size = 0
            return 
        
        self.head = Node(items[0])
        
        if len(items) == 1:
            self.size = 1
            self.tail = self.head
            return 
        
        current = Node(items[1])
        current.prev = self.head
        self.head.next = current
        
        self.size = 2
        while self.size < len(items):
            new_node = Node(items[self.size])
            new_node.prev = current
            current.next = new_node
            current = new_node
            self.size += 1
            
        self.tail = current
        
    def __len__(self):
        """Method to know the size"""
        return self.size
    
    def __getitem__(self, index: int) -> Any:
        if not isinstance(index, int):
            raise TypeError("The index must be an integer")
        
        if abs(index) > self.size or index == self.size:
            raise IndexError("Linked List index out of range") 
        
        count = 0
        index = index % self.size
        
        current = self.head
        while count != index:
            current = current.next 
            count += 1
        return current.data
        
    def append(self, item: Any) -> None:
        """Method to add an item to the end of the linked list"""
        new_node = Node(item)
        
        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = self.tail = new_node
            
        self.size += 1
            
    def appendleft(self, item: Any) -> None:
        """Method to add an item to the beginning of the array"""
        new_node = Node(item)
        
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
            
        self.size += 1
            
    def pop(self) -> Any:
        """Method to remove an element at the end of the linked list"""
        if self.head is None:
            raise IndexError("There is no node to delete")
        
        popped = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None 
        self.size -= 1
        return popped
        
    def popleft(self) -> Any:
        """Method to remove an element at the beginning of the linked list"""
        if self.head is None:
            raise IndexError("There is no node to delete")
        
        popped = self.head 
        self.head = self.head.next 
        self.head.prev = None 
        self.size -= 1
        return popped
    
    def extend(self, items: Iterable[Any]) -> None:
        """Method to add several elements to the linked list"""
        try:
            for item in items: 
                self.append(item)   
        except TypeError as error:
            raise error
        
    def rotate(self, number: int) -> None:
        """Method to rotate the linked list"""
        number = number % self.size
        
        if self.size == 0 or number == 0 or abs(number) == self.size:
            return 
        
        current = self.head 
        count = 0

        while count < self.size - number:
            current = current.next
            count += 1
        
        self.tail.next = self.head
        self.tail = current.prev
        self.tail.next = None
        self.head = current
        self.head.prev = None
        
    def clear(self):
        """Method to clear all the list"""
        self.__create_items([])
     
    def __repr__(self) -> str:
        if self.head is None:
            return "[]"
        result = "["
        current = self.head
        while current:
            result = result + str(current.data) + ", "
            current= current.next
            
        return result[:-2] + "]" if len(result) > 2 else result + "]"
