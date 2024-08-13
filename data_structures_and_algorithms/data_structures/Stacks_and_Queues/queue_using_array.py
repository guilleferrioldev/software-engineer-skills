### Queues implementation using Arrays

from typing import Any

class Queue:
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