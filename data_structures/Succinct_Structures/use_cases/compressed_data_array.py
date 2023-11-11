class SuccinctArray:
    def __init__(self, input_array):
        self.bit_vector = 0
        self.bits = [0]
        
        for bit in input_array:
            self.bit_vector = (self.bit_vector << 1) | bit
            self.bits.append(self.bits[-1] + bit)

    def access(self, index):
        return self.bits[index]
    
    def rank(self, index):
        return self.bits[index] - self.bits[0]
    
    def select(self, value, occurrence):
        indices = [i for i, bit in enumerate(self.bits) if bit == value]
        if len(indices) < occurrence:
            return -1
        return indices[occurrence - 1]

# Example usage
data = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
compressed_array = SuccinctArray(data)

# Accessing the 5th element
accessed_value = compressed_array.access(4)
print("Accessed value at index 4:", accessed_value)

# Getting the rank of 1 at index 7
rank_value = compressed_array.rank(7)
print("rank of 1 at index 7:", rank_value)

# Getting the select index of 0 at the 3rd occurrence
select_index = compressed_array.select(0, 3)
print("Select index of 0 at the 3rd occurrence:", select_index)
