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


def KMP(text, pattern):
    if not pattern: # pattern == "" 
        return 0
        
    lps = compute_lps_array(pattern)  # Compute the lps array for the pattern
    
    matches = []
    i = 0  # Pointer for the text
    j = 0  # Pointer for the pattern
    while i < len(text):
        # If there is a match
        if text[i] == pattern[j]:
            # Advance both pointers
            i, j = i + 1, j + 1
        # If j reaches the length of the pattern
        if j == len(pattern):
            # Add the starting index of the match to the matches list
            matches.append(i - j)
            # Update j using the LPS array
            j = lps[j - 1]
        # If there is a mismatch
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                # Update j using the LPS array
                j = lps[j - 1]
            else:
                # Move to the next character in the text
                i += 1
    return matches


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