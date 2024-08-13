from typing import Self, Optional, List, Set

class Node:
    """Node implementation"""
    def __init__(self, substring: str = "", children: Optional["Node"] = None) -> None:
        self.substring = substring
        self.children = children or []

class SuffixTree:
    """Suffix Tree implementation"""
    def __init__(self, text: str) -> None:
        self.text = text + "$"
        self.nodes = [Node()]
        
        for i in range(len(self.text)):
            self.add_suffix(self.text[i:])

        self._suffixes = []
        self._collect_suffixes(0, "", self._suffixes)

    def add_suffix(self, suffix: str) -> None:
        """Ukkonen's Suffix Tree Algorithm"""
        node_index = 0
        i = 0
        while i < len(suffix):
            current_char = suffix[i]
            child_index = 0
            while True:
                children = self.nodes[node_index].children
                if child_index == len(children):
                    # There is no matching child, the rest of the suffix becomes a new node
                    new_node_index = len(self.nodes)
                    self.nodes.append(Node(suffix[i:], []))
                    self.nodes[node_index].children.append(new_node_index)
                    return
                next_node_index = children[child_index]
                if self.nodes[next_node_index].substring[0] == current_char:
                    break
                child_index = child_index + 1
            # find prefix of remaining suffix in common with child
            common_substring = self.nodes[next_node_index].substring
            j = 0
            while j < len(common_substring):
                if suffix[i + j] != common_substring[j]:
                    # Split the node next_node_index
                    new_node_index = next_node_index
                    # New node for the common part
                    next_node_index = len(self.nodes)
                    self.nodes.append(Node(common_substring[:j], [new_node_index]))
                    self.nodes[new_node_index].substring = common_substring[j:] # The old node loses the common part
                    self.nodes[node_index].children[child_index] = next_node_index
                    break  # Continuar bajando en el árbol
                j = j + 1
            i = i + j  # Move beyond the common part
            node_index = next_node_index  # Continue down the tree

    def _collect_suffixes(self, node_index: int, current_suffix: str, suffixes: List) -> None:
        """Method to return all suffixes"""
        children = self.nodes[node_index].children
        if len(children) == 0:
            suffix = current_suffix + self.nodes[node_index].substring
            if suffix != "$":
                suffixes.append(suffix.replace("$", ""))
        else:
            for child in children:
                self._collect_suffixes(child, current_suffix + self.nodes[node_index].substring, suffixes)
                
    def __eq__(self, other: Self) -> Optional[Set]: 
        """Method to return all suffixes in common whith another Suffix Tree"""
        if isinstance(other, SuffixTree):
            result = set(self._suffixes).intersection(set(other._suffixes)) 
            return result if result else None

    def __repr__(self) -> str:
        return f"{self._suffixes}"