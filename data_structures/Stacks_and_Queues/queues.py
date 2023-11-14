### Queues

from typing import Any, Self

class QueueArray:
    """Implementation using Arrays"""
    def __init__(self, size: int = None) -> None:
        self.items = []
        self.front = self.rear = 0
        self.size = size
    
    def enqueue(self, data: Any) -> None:
        """Method to enqueue an element"""
        if self.size == self.rear:
            return "Queue is full"
        self.items.append(data)
        self.rear += 1
    
    def dequeue(self) -> Any:
        """ Method to dequeue an element"""
        if self.front == self.rear:
            return "Queue is empty"
        
        data = self.items.pop(0) 
        self.rear -= 1
        return data
  
    def __repr__(self) -> str:
        return str(self.items)


######################################################################################################
class Node:
    """Implementation of the node"""
    def __init__(self, data: Any = None, next: Self = None, prev: Self = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class QueueLinkedList:
    """Implementation using linked lists"""
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, data: Any) -> None:
        """Method to eneque an element"""
        new_node = Node(data)
        
        if self.front is None:
            self.front = new_node
            self.rear = self.front
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        
    def dequeue(self) -> Node:
        """Method to dequeue an element"""
        if self.size < 1:
            return "Queue is empty"
        
        data = self.front.data
        
        if self.size == 1:
            self.front = self.rear = None
        elif self.size > 1:
            self.front = self.front.next
            self.front.prev = None
        
        self.size -= 1 
        return data

    def __repr__(self) -> str:
        current = self.front
        result = "["
        while current:
            result = result + str(current.data) + ", "
            current = current.next
        return result[:-2] + "]" if len(result) > 1 else result + "]"


#################################################################################################
class QueueStacks:
    """Implementation using stack"""
    def __init__(self) -> None :
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, data: Any) -> None:
        """Method to enqueue an element"""
        self.stack1.append(data)
    
    def dequeue(self):
        """Method to dequeue an element"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("No element to dequeue")
            return
        return self.stack2.pop()

    def __repr__(self):
        return f"stack1={self.stack1}, stack2={self.stack2})"
