from collections import deque
from typing import List

class Node:
    """Node implementation"""
    def __init__(self) -> None:
        self.children = {}
        self.is_leaf = False
        
class Trie:
    """Trie implementation"""
    def __init__(self, *words: str) -> None:
        self.root = Node()
        
        if not words:
            return 
        
        for word in words:
            self.insert(word)        
        
    def insert(self, word: str) -> None:
        """Insert words in the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
            
        node.is_leaf = True
        
    def search(self, word: str) -> bool:
        """Search if a word is in the Trie"""
        node = self.root 
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return node.is_leaf
    
    def startwith(self, prefix: str) -> bool:
        """Find if there is a word that exist in the Trie starts with the prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return True
    
    def _all_words(self) -> List[str]:
        """Return a list of all words present in the Trie"""
        words = []

        def dfs(node: Node, prefix: str) -> None:
            if node.is_leaf:
                words.append(prefix)
            
            for char, child_node in node.children.items():
                dfs(child_node, prefix + char)

        dfs(self.root, "")
        return words
        
    def __repr__(self) -> str:
        return f"{self._all_words()}"