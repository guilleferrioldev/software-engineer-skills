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

def pfun(pattern):          # function to generate prefix function for the given pattern
    n = len(pattern)        # length of the pattern
    prefix_fun = [0]*(n)    # initialize all elements of the list to 0
    k = 0
    for q in range(2,n):
        while k>0 and pattern[k+1] != pattern[q]:
            k = prefix_fun[k]
        if pattern[k+1] == pattern[q]:      # If the kth element of the pattern is equal to the qth element
            k += 1                          # update k accordingly
        prefix_fun[q] = k
    return prefix_fun                       # return the prefix function


def KMP_Matcher(text,pattern):              # KMP matcher function
    m = len(text)
    n = len(pattern)
    flag = False
    text = '-' + text                       # append dummy character to make it 1-based indexing
    pattern = '-' + pattern                 # append dummy character to the pattern also
    prefix_fun = pfun(pattern)              # generate prefix function for the pattern
    q = 0
    for i in range(1,m+1):
        while q>0 and pattern[q+1] != text[i]:      # while pattern and text are not equal, decrement the value of q if it is > 0
            q = prefix_fun[q]
        if pattern[q+1] == text[i]:                 # if pattern and text are equal, update value of q
            q += 1
        if q == n:                                      # if q is equal to the length of the pattern, it means that the pattern has been found.
            print("Pattern occours with shift",i-n)     # print the index, where first match occours.
            flag = True
            q = prefix_fun[q]
    if not flag:
        print('\nNo match found')
