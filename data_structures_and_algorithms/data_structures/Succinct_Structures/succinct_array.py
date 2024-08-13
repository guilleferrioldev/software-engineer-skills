"""
A succinct array is a compact and efficient data structure that represents an array of bits in which the number of 1s (or 0s)
between any pair of indexes can be queried efficiently. These structures are commonly used in applications where efficient 
memory usage is needed, such as in search engines, data compression, and more.

In this implementation, input_array is the array of bits we want to represent, and SuccinctArray constructs a succinct array from
this array. The rank_query function returns the number of ones up to a given index, while rank_query_range returns the number of
ones in a given range.
"""

class SuccinctArray:
    def __init__(self, input_array):
        # We initialize `bit_vector` as 0 and `rank` as a list with the first element being zero
        self.bit_vector = 0
        self.rank = [0]
        # We then iterate through the `input_array`, and for each bit, we shift the `bit_vector` one place 
        # to the left and append the current bit to it.
        for bit in input_array:
            self.bit_vector = (self.bit_vector << 1) | bit
            # We also calculate and store the cumulative count of 1s encountered so far using the `rank` list.
            self.rank.append(self.rank[-1] + bit)

    # This method takes an `index` as input and returns the count of 1s up to that index using the `rank` list
    def rank_query(self, index):
        return self.rank[index]

    # This method takes `start` and `end` indices as input and returns the count of 1s in the range from `start` to `end` using the `rank` list.
    def rank_query_range(self, start, end):
        return self.rank[end] - self.rank[start]
    
if __name__ == "__main__":
    arr = [1, 0, 1, 1, 0, 1, 0, 1]
    succinct_array = SuccinctArray(arr)
    print(succinct_array.rank_query_range(2, 5))  # Output: 3
    print(succinct_array.rank_query(1)) # Output 1
