# The Knuth-Morris-Pratt algorithm

# Time Complexity: O(m+n)
# Space Complexity: O(m)

"""
The KMP pattern matching algorithm detects overlaps in the pattern itself so that it avoids unnecessary comparisons. The main idea behind the KMP algorithm
is to detect how much the pattern should be shifted, based on the overlaps in the patterns. The algorithm works as follows:
- 1. First, we precompute the prefix function for the given pattern and initialize a counter q that represents the number of characters that matched. 

- 2. We start by comparing the first character of the pattern with the first character of the text string, and if this matches, then we increment the counter
q for the pattern and the counter for the text string, and we compare the next character.

- 3. If there is a mismatch, then we assign the value of the precomputed prefix function for q to the index value of q.

- 4. We continue searching the pattern in the text string until we reach the end of the text, that is, if we do not find any matches. If all of the characters 
in the pattern are matched in the text string, we return the position where the pattern is matched in the text and continue to search for another match.
"""

from typing import List

def KMP(text: str, pattern: str) -> int:
    if not pattern: # pattern == "" 
        return 0
        
    lps = compute_lps_array(pattern)  # Compute the lps array for the pattern

    i = 0  # Pointer for the text
    j = 0  # Pointer for the pattern
    while i < len(text):
        # If there is a match
        if text[i] == pattern[j]:
            # Advance both pointers
            i, j = i + 1, j + 1
        # If there is no match
        else:
            if j == 0:
                # If j is 0, only advance the text pointer
                i += 1
            else:
                # Use information from the lps table to move the pattern pointer backward
                j = lps[j - 1]
        # If j reaches the length of the pattern
        if j == len(pattern):
            # A complete match is found, so return the position where it starts
            return i - len(pattern)
    # If no match is found, return -1
    return -1

def compute_lps_array(pattern: str) -> List[int]:
    # Longest-Prefix-Suffix (Table lps)
    lps = [0] * len(pattern) 

    # Initialize prevLPS to 0 and index to 1
    prevLPS, index = 0, 1
    while index < len(pattern):
        # If the current character in the pattern matches the character at position prevLPS
        if pattern[index] == pattern[prevLPS]:
            # Assign the value prevLPS + 1 to the lps table at position index
            lps[index] = prevLPS + 1
            # Increment prevLPS
            prevLPS += 1
            # Increment index
            index += 1
        # If prevLPS is already 0
        elif prevLPS == 0:
            # Assign 0 to the lps table at position index
            lps[index] = 0
            # Increment index
            index += 1
        # If there is no match and prevLPS is not 0
        else:
            # Update prevLPS using the value from lps at position prevLPS - 1
            prevLPS = lps[prevLPS - 1]
    
    return lps


s1 = KMP("sadbutsad", "sad")
s2 = KMP("leetcode", "leeto")
s3 = KMP("hello", "ll")
    
print(s1, s2, s3)
