# Queue implementation using stacks

"""
To achieve this, we can use two stacks. When we want to sneak an element, we simply add it to the first stack. 
When we want to dequeue an element, we move all the elements from the first stack to the second stack, which 
reverses the order, and then pop the top element from the second stack.
"""

from typing import Any

class Queue:
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
