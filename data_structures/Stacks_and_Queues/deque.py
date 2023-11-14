### Deque 
from typing import Any, List, Self, Iterable

class DequeArray:
    """Implementation using Array"""
    def __init__(self, items: List = None) -> None:
        if items is not None:
            self.items = items
        else:
            self.items = []
        
    def append(self, item: Any) -> None:
        """Method to add an item to the end of the array"""
        self.items.append(item)
        
    def appendleft(self, item: Any) -> None:
        """Method to add an item to the beginning of the array"""
        self.items.insert(0, item)
        
    def pop(self) -> Any:
        """Method to remove an element at the end of the array"""
        return self.items.pop()
        
    def popleft(self) -> Any:
        """Method to remove an element at the beginning of the array"""
        return self.items.pop(0)
    
    def extend(self, items: Iterable) -> Any:
        """Method to add several elements to the array"""
        self.items.extend(items)
        
    def rotate(self, number: int) -> None:
        """Method to rotate the array"""
        self.items = self.items[-number:] + self.items[:-number]
             
    def __getitem__(self, item: int) -> Any:
        return self.items[item]
        
    def __repr__(self):
        return str(self.items)
        

#############################################################################################
class Node:
    """Implementation of the node"""
    def __init__(self, data: Any = None, next: Self = None, prev: Self = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class DequeLinkedList:
    """Implementation using Linked List"""
    def __init__(self, items: List = None) -> None:
        if items is not None:
            self.__create_items(items)
        else:
            self.__create_items([])
        
    def __create_items(self, items: List) -> None:
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
    
    def __getitem__(self, index: int) -> Any:
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
    
    def extend(self, items: Iterable) -> None:
        """Method to add several elements to the linked list"""
        try:
            for item in items: 
                self.append(item)   
        except TypeError as error:
            raise error
        
    def rotate(self, number: int) -> None:
        """Method to rotate the linked list"""
        if self.size == 0:
            return 
        
        current = self.head 
        counter = 0 
        while counter < number and current is not None:
            current = current.next
            counter += 1

        if current is None:
            return

        self.tail = current

        while current.next is not None:
            current = current.next

        current.next = self.head
        self.head.prev = current

        self.head = self.tail.next
        self.head.prev = None
        
        self.tail.next = None
     
    def __repr__(self) -> str:
        if self.head is None:
            return "[]"
        result = "["
        current = self.head
        while current:
            result = result + str(current.data) + ", "
            current= current.next
            
        return result[:-2] + "]" if len(result) > 2 else result + "]"
            
x = DequeLinkedList([6,7,8])
x.append(1)
x.extend([2,3,5])

print(x)

        
    