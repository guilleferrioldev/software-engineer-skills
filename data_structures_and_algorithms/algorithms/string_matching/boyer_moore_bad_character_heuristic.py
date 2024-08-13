# The Boyer-Moore bad character heuristic algorithm

# Time Complexity : O(n x m)
# Auxiliary Space: O(1)

"""
The Boyer-Moore pattern matching algorithm is another such algorithm (along with the KMP algorithm) that further improves the performance of pattern 
matching by skipping comparisons using different methods. We have to understand the following concepts in order to understand the Boyer-Moore algorithm:
- 1. In this algorithm, we shift the pattern in the direction from left to right, similar to the KMP algorithm.

- 2. We compare the characters of the pattern and the text string from right to left, which is the opposite of what we do in the case of the KMP algorithm.

- 3. The algorithm skips the unnecessary comparisons by using the good suffix and bad character shift heuristics. These heuristics themselves find the 
possible number of comparisons that can be skipped. We slide the pattern over the given text with the greatest offsets suggested by both of these heuristics

The Boyer-Moore algorithm compares the pattern and the text string in the direction of right to left. It uses the bad character heuristic to shift the pattern,
where we start comparing character by character from the end of the pattern, and if they match then we compare the second to-last character, and if that also 
matches, then the process is repeated until the entire pattern is matched or we get a mismatch

The mismatched character of the text is also known as a bad character. If we get any mismatch in this process, we shift the pattern according to one of the following conditions:
- 1. If the mismatched character of the text does not occur in the pattern, then we shift the pattern next to the mismatched character.

- 2. If the mismatched character has one occurrence in the pattern, then we shift the pattern in such a way that we align with the mismatched character.

- 3. If the mismatched character has more than one occurrence in the pattern, then we make the most minimal shift possible to align the pattern with that character.
"""

 
def badCharHeuristic(string, size):
    # Initialize all occurrence as -1
    badChar = [-1]*256
 
    # Fill the actual value of last occurrence
    for index in range(size):
        badChar[ord(string[index])] = index;
 
    # return initialized list
    return badChar
 
def boyer_moore(text, pattern):
    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pattern, len(pattern))
 
    # shift of the pattern with respect to text
    shift = 0
    while(shift <= len(text)-len(pattern)):
        length = len(pattern)-1
 
        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while length >= 0 and pattern[length] == text[shift+length]:
            length -= 1
 
        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if length<0:
            print("Pattern occur at shift = {}".format(shift))
            shift += (len(pattern)-badChar[ord(text[shift+len(pattern)])] if shift+len(pattern)<len(text) else 1)
        else:
            shift += max(1, length-badChar[ord(text[shift+length])])


