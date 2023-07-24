# The Rabin-Karp algorithm

# Time Complexity: O(nm), where m is the length of the pattern and n is the length
# Auxiliary Space: O(1).

"""
Rabin-Karp algorithm is an algorithm used for searching/matching patterns in the text using a hash function. Unlike Naive string matching algorithm, 
it does not travel through every character in the initial phase rather it filters the characters that do not match and then performs the comparison.

A hash function is a tool to map a larger input value to a smaller output value. This output value is called the hash value.

The Rabin-Karp pattern matching algorithm works as follows:
- 1. First, we preprocess the pattern before starting the search, that is, we compute the hash value of the pattern of length m and the hash values of all 
the possible substrings of the text of length m. The total number of possible substrings would be (n-m+1). Here, n is the length of the text.

- 2. We compare the hash value of the pattern with the hash value of the substrings of the text one by one.

- 3. If the hash values are not matched, then we shift the pattern by one position.

- 4. If the hash value of the pattern and the hash value of the substring of the text match, then we compare the pattern and substring character by character 
to ensure that the pattern is actually matched in the text.

- 5. We continue the process of steps 2-5 until we reach the end of the given text string.
"""


def generate_hash(text, pattern):
    ord_text = [ord(i) for i in text]                              # stores unicode value of each character in text 
    ord_pattern = [ord(j) for j in pattern]                        # stores unicode value of each character in pattern
    len_text = len(text)                                           # stores length of the text 
    len_pattern = len(pattern)                                     # stores length of the pattern
    len_hash_array = len_text - len_pattern + 1                    # stores the length of new array that will contain the hash values of text
    hash_text = [0]*(len_hash_array)                               # Initialize all the values in the array to 0.
    hash_pattern = sum(ord_pattern)                                                
    for i in range(0,len_hash_array):                              # step size of the loop will be the size of the pattern
        if i == 0:                                                 # Base condition
            hash_text[i] = sum(ord_text[:len_pattern])             # initial value of hash function
        else:
            hash_text[i] = ((hash_text[i-1] - ord_text[i-1]) + ord_text[i+len_pattern-1])   # calculating next hash value using previous value
    return [hash_text, hash_pattern]                               # return the hash values



def Rabin_Karp_Matcher(text, pattern):
    text = str(text)                                                     # convert text into string format
    pattern = str(pattern)                                               # convert pattern into string format
    hash_text, hash_pattern = generate_hash(text, pattern)               # generate hash values using generate_hash function
    len_text = len(text)                                                 # length of text
    len_pattern = len(pattern)                                           # length of pattern
    flag = False                                                         # checks if pattern is present atleast once or not at all
    for i in range(len(hash_text)):                         
        if hash_text[i] == hash_pattern:                                 # if the hash value matches
            count = 0                                                    # count stores the total characters upto which both are similar
            for j in range(len_pattern):                                 
                if pattern[j] == text[i+j]:                              # checking equality for each character
                    count += 1                                           # if value is equal, then update the count value
                else:
                    break
            if count == len_pattern:                                     # if count is equal to length of pattern, it means match has been found
                    flag = True                                          # update flag accordingly
                    print('Pattern occours at index',i)
    if not flag:                                                         # if pattern doesn't match even once, then this if statement is executed
        print('Pattern is not at all present in the text')
