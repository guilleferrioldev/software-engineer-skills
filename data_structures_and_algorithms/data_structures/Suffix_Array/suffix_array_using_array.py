# Suffix array implementation using Array

from typing import List

class SuffixArray:
    """Suffix array implementation using Array"""
    def __init__(self, text: str) -> None:
        self.text = text
        self.suffix_array = self.__create_suffix_array()
        
    def __create_suffix_array(self) -> List:
        """Create the suffix array"""
        suffixes =  sorted([(self.text[index:], index) for index in range(len(self.text))])
        
        return [index for suffix, index in suffixes]
    
    def __repr__(self) -> str:
        return f"{self.suffix_array}"