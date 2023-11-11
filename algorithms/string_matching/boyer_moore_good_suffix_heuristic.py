# Boyer-Moore good suffix heuristic algorithm

"""
The bad character heuristic does not always provide good suggestions for shifting the pattern. The Boyer-Moore algorithm also uses the good 
suffix heuristic to shift the pattern over the text string, which is based on the matched suffix. In this method, we shift the pattern to the
right in such a way that the matched suffix of the pattern is aligned with another occurrence of the same suffix in the pattern

It works like this: we start by comparing the pattern and the text string from right to left, and if we find any mismatch, then we check the 
occurrence of the suffix in the pattern that has been matched so far, which is known as a good suffix

In such situations, we shift the pattern in such a way that we align another occurrence of the good suffix to the text. The good suffix heuristic 
has two main cases:
- 1. The matching suffix has one or more occurrences in the pattern 

- 2. Some part of the matching suffix is present at the start of the pattern (this means that the suffix of the matched suffix exists as the prefix of the pattern)
"""

# preprocessing for strong good suffix rule
def preprocess_strong_suffix(shift, bpos, pat, m):  
    # m is the length of pattern
    i = m
    j = m + 1
    bpos[i] = j
  
    while i > 0:
        while j <= m and pat[i - 1] != pat[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
  
            # Update the position of next border
            j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j 

# Preprocessing for case 2
def preprocess_case2(occurrences, bpos, pattern, length):
    j = bpos[0]
    for index in range(length + 1):
        if occurrences[index] == 0:
            occurrences[index] = j
        if index == j:
            j = bpos[j]
  
def boyer_moore(text, pattern):
  
    # s is shift of the pattern with respect to text
    shift = 0
    
    bpos = [0] * (len(pattern) + 1)
    # initialize all occurrence of shift to 0
    occurrences = [0] * (len(pattern) + 1)
  
    # do preprocessing
    preprocess_strong_suffix(occurrences, bpos, pattern, len(pattern))
    preprocess_case2(occurrences, bpos, pattern, len(pattern))
  
    while shift <= len(text) - len(pattern):
        length = len(pattern) - 1
        while length >= 0 and pattern[length] == text[shift + length]:
            length -= 1
        if length < 0:
            print("pattern occurs at shift = %d" % shift)
            shift += occurrences[0]
        else:
            shift += occurrences[length + 1]
