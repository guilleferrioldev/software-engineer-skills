class Node:
    def __init__(self, start, end, suffix_link=None):
        self.start = start 
        self.end = end 
        self.suffix_link = suffix_link 
        self.children = {}  

class SuffixTree:
    def __init__(self, string):
        self.root = Node(-1, -1)  
        self.string = string 
        self.build()  

    def build(self):
        active_node = self.root
        active_edge = 0
        active_length = 0
        remainder = 0

        for index in range(len(self.string)):
            remainder += 1
            last_created_node = None

            while remainder > 0:
                if active_length == 0:
                    active_edge = index

                if self.string[index] not in active_node.children:
                    leaf_node = Node(index, len(self.string)-1)
                    active_node.children[self.string[index]] = leaf_node
                    if last_created_node is not None:
                        last_created_node.suffix_link = active_node
                        last_created_node = None

                else:
                    next_node = active_node.children[self.string[active_edge]]
                    next_length = next_node.end - next_node.start + 1
                    if active_length >= next_length:
                        active_edge += next_length
                        active_length -= next_length
                        active_node = next_node
                        continue

                    if self.string[next_node.start + active_length] == self.string[index]:
                        active_length += 1
                        if last_created_node is not None and active_node != self.root:
                            last_created_node.suffix_link = active_node
                            last_created_node = None
                        break

                    split_node = Node(next_node.start, next_node.start + active_length - 1)
                    split_node.children[self.string[index]] = Node(index, len(self.string)-1)
                    split_node.children[self.string[next_node.start + active_length]] = next_node
                    next_node.start += active_length
                    active_node.children[self.string[active_edge]] = split_node

                    if last_created_node is not None:
                        last_created_node.suffix_link = split_node
                    last_created_node = split_node

                remainder -= 1
                if active_node == self.root and active_length > 0:
                    active_length -= 1
                    active_edge = index - remainder + 1
                elif active_node != self.root:
                    active_node = active_node.suffix_link
                    
    def get_all_suffixes(self, node, suffixes):
        if node.start != -1 and node.end != -1:
            suffixes.append(self.string[node.start : node.end + 1])
        for child in node.children.values():
            self.get_all_suffixes(child, suffixes)

    def __repr__(self):
        suffixes = []
        self.get_all_suffixes(self.root, suffixes)
        return f"Suffices: {suffixes}"
                    

input_string = "banana"
suffix_tree = SuffixTree(input_string)
print(suffix_tree)