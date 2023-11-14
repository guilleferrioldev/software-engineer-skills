# Stacks implemnetation using Array-based

from typing import Any

class StackOverflowError(Exception):
    pass

class Stack:
    """Stacks implemnetation using Array-based"""
    def __init__(self, size: int = float("inf")) -> None:
        self.items = []
        self.top = -1
        self.size = size
    
    def isEmpty(self) -> bool:
        """Method to know if a stack is empty"""
        return self.items == []
    
    def push(self, item: Any) -> None | Exception:
        """ Method to add an element """
        if self.top >= self.size -1 :
            raise StackOverflowError()    
        self.top += 1
        self.items.append(item)
    
    def pop(self) -> str | Any:
        """Method to delete an element """
        if self.top == -1:
            return "Stack Underflow"    
        self.top -= 1
        return self.items.pop()
    
    def peek(self) -> str | Any:
        """Method to check the top element"""
        if self.top == -1:
            return "Stack is empty"
        return self.items[self.top]

    def __repr__(self) -> str:
        return f"{self.items}"