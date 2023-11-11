### Single Linked List

from typing import Any, Self

class Node:
    """Node implementation"""
    def __init__(self, data: Any = None) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Implementation of the single linked list"""
    def __init__ (self, head = None, tail = None, size = 0) -> None:
        self.head = head
        self.tail = tail
        self.size = size
    
    def __iter__(self) -> None:
        """Method to iterate the linked list"""
        current = self.head
        
        while current:
            value = current.data
            current = current.next
            yield value
            
    def __len__(self):
        return self.size
            
    def __ge__(self, other: Self) -> bool:
        """Method to compare linked lists by size"""
        if isinstance(other, SinglyLinkedList):
            return self.size >= other.size
        
    def __gt__(self, other: Self) -> bool:
        """Method to compare linked lists by size"""
        if isinstance(other, SinglyLinkedList):
            return self.size > other.size


    def __add__(self, other: Self) -> Self: 
        """Method to add two linked lists"""       
        if self.tail:
            self.tail.next = other.head
            self.tail = other.tail
        else:
            self.head = other.head
            self.tail = other.tail
        
        self.size += other.size
        
        return SinglyLinkedList(head = self.head, tail = other.tail, size = self.size)
    
    def __sub__(self, number: int) -> None:
        """Method to delete the lastest k nodes of the linked list"""
        if not isinstance(number, int):
            raise TypeError(f"The linked list can only be subtracted with an integer, not {type(number).__name__}")
        
        if self.head and number <= self.size:
            current = self.head
            count = 0
                
            while count < (self.size - number - 1):
                current = current.next 
                count += 1

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = current
                self.tail.next = None 
                
            self.size -= number
                
            return SinglyLinkedList(head = self.head, tail = self.tail, size = self.size)
        else:
            raise ValueError(f"The value has to be integer and less than the dimension, which is {self.size}")
                         
    def __getitem__(self, index_or_value: Any) -> Any | Exception:
        """Get item from a index with slice"""
        if not isinstance(index_or_value, int):
            return self._get_index(value = index_or_value)
        
        index = index_or_value
        if self.head and abs(index) > self.size or index == self.size:
            try:
                return self._get_index(value = index_or_value)
            except:
                raise IndexError("Linked List index out of range and the value does not exists") 
            
        if index >= 0:            
            return self._get_value_by_index(index)
               
        index += self.size 
        return self._get_value_by_index(index)
    
    def _get_index(self, value: Any) -> None:
        current = self.head 
        index = 0
        
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
            
        raise Exception
        
    def _get_value_by_index(self, index) -> Any:
        """Auxiliary method to obtain a node in a position"""
        count = 0
        current = self.head
        
        while count < self.size - 1:
            if count == index:
                break 
            current = current.next 
            count += 1
        
        return current.data
    
    def __setitem__(self, index: int, data: Any) -> None:
        """Add element in a position using slice"""
        if not isinstance(index, int):
            raise TypeError(f"Lindked list indices must be integers or slices, not {type(index).__name__}")
        
        if abs(index) > self.size or index == self.size:
            raise IndexError("Linked List index out of range")
        
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index > 0:
            self._set_value_by_index(index, new_node)
        else:
            index += self.size
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            elif index == self.size -1:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = None
            else:
                self._set_value_by_index(index, new_node)
                       
        self.size += 1
        
    def _set_value_by_index(self, index: int, new_node: Node) -> None:
        """Auxiliary method to add node in a position"""
        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            count += 1 

        new_node.next = current.next
        current.next = new_node
            
    def pop(self) -> Any:
        """Method to delete the last element of the linked list"""
        if self.head is None:
            raise IndexError("The linked list is empty")
        
        if self.size == 1:
            value = self.tail.data
            self.head = None
            self.tail = None
        else:
            current = self.head 
            while current.next != self.tail:
                current = current.next
                
            value = current.data
            current.next = None
            self.tail = current
            
        self.size -= 1

        return value
    
    def popleft(self) -> Any:
        """Method to delete the first element of the linked list"""
        if self.head is None:
            raise IndexError("The linked list is empty")
        
        value = self.head
        self.head = self.head.next
        self.size -= 1
        
        return value.data
        
    def append(self, data: Any) -> None:
        """Method to insert an node at the end of the linked list""" 
        node = Node(data)
        
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
            
        self.size += 1
    
    def push(self, data: Any) -> None:
        """Method to insert a node at the beginning of the linked list"""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def delete(self, index_or_value: Any) -> None: 
        if not isinstance(index_or_value, int):
            index_or_value = self._get_index(value = index_or_value)  
            
        if abs(index_or_value) > self.size or index_or_value > self.size - 1:
            raise IndexError("Linked List index out of range")
        
        if self.head is None:
            raise IndexError("The linked list is empty")
            
        if index_or_value == 0:
            self.popleft()
        elif index_or_value > 0:
            if index_or_value == self.size - 1:
                self.pop()
            self._delete_value_by_index(index_or_value)
        else:
            index_or_value += self.size
            if index_or_value == 0:
                self.popleft()
            self._delete_value_by_index(index_or_value)
            
        self.size -= 1
    
    def _delete_value_by_index(self, index: int) -> None:
        """Auxiliary method to add node in a position"""
        current = self.head
        previous = self.head
        count = 0
        while current:
            if count == index:
                previous.next = current.next 
                return  
            count += 1
            previous = current
            current = current.next
        
        
    def clear(self) -> None:
        """Method to clear the list"""
        self.tail = None
        self.head = None
        self.size = 0
    
    def reverse(self) -> None:
        """Method to reverse the list"""
        prev = None
        
        while self.head is not None:
            self.head.next , prev, self.head = prev, self.head, self.head.next
        self.head = prev   
        
    def __repr__(self) -> str:
        """Method to print the list"""
        current = self.head
        result = ""
        
        while current:
            result = result + str(current.data) + " -> "
            current = current.next
        
        return result + "end"
    
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append("a")
    linked_list.push(0)
    linked_list.push("g")
    
    linked_list_2 = SinglyLinkedList()
    linked_list_2.append(5)
    linked_list_2.append(2)
    
    linked_list + linked_list_2
    
    print(linked_list)
    
    print("5th position ->", linked_list[5]) # -> 2 5th position because first it looks for the position and if it doesn't find it it will
                                           # look for the given value
    print("Pop ->", linked_list.pop()) # Delete the value 2
    print("Popleft ->", linked_list.popleft())
    print("Position of the value 5 ->", linked_list[5]) # -> 4 because it returns the position if the value is in the linked list
    
    linked_list[1] = 5
    
    print(linked_list == linked_list_2)
    print(linked_list >= linked_list_2)
    print(linked_list <= linked_list_2)
    print(linked_list > linked_list_2)
    print(linked_list < linked_list_2)
    
    linked_list.delete(0)
    
    print(len(linked_list))
    for i in linked_list:
        print(i)
    
    
    
