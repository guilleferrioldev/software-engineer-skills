# Red-Black Tree implementation using linked list

from typing import Any

class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None 
        self.right = None 
        self.height = 1
        
class RedBlackTree:
    def __init__(self) -> None:
        self.root = None 
    