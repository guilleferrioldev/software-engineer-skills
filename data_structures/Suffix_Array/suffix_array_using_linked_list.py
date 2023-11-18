# Suffix array implementation using Linked List

from typing import Self

class Node:
    """Node implementation"""
    def __init__(self, suffix: str, index: int) -> None:
        self.suffix = suffix
        self.index = index
        self.next = None
        
class SuffixArray:
    """Suffix array implementation using Linked List"""
    def __init__(self, text: str) -> None:
        self.text = text
        self.head = None
        self.__create_suffix_array()
        
    def __create_suffix_array(self) -> None:
        """Create the suffix array"""
        suffixes = sorted([(self.text[i:], i) for i in range(len(self.text))])
        
        for suffix, index in suffixes:
            self.add_suffix(suffix, index)
        
    def add_suffix(self, suffix: str, index: int) -> None:
        """Add new node to the linked list"""
        new_node = Node(suffix, index)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __repr__(self) -> str:
        suffix_array = []
        current = self.head
        while current:
            suffix_array.append(current.index)
            current = current.next
        return f"{suffix_array}"
