# Stack implementation using queue

"""
When push is called to add an element, we first add it to the end of the queue and then rotate the queue so that this new element 
is the first. In this way, the last element added becomes the first element accessed, simulating the behavior of a stack.
"""

from typing import Any, List

class Stack:
    def __init__(self, queue: List = None) -> None:
        self.__rotate_queue(queue)
            
    def __rotate_queue(self, queue) -> None:
        self.queue = []
        
        if queue is None:
            return
        
        for index in range(len(queue) -1, -1, -1):
            self.queue.append(queue[index])
    
    def is_empty(self) -> bool:
        """Method to know if a stack is empty"""
        return len(self.queue) == 0
    
    def push(self, item: Any) -> None:
        """ Method to add an element """
        self.queue.append(item)
       
        # Rotate the queue so that the last item added is the first in the queue
        for _ in range(len(self.queue) -1):
            self.queue.append(self.queue.pop(0))
        
    def pop(self) -> Any:
        """Method to delete an element """
        if self.is_empty():
            return 
        return self.queue.pop(0)
    
    def peek(self) -> Any:
        """Method to check the top element"""
        if self.is_empty():
            return 
        return self.queue[0]
        
    def __repr__(self) -> str:
        return f"{self.queue}"