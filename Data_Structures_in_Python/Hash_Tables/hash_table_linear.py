###  Linear Probing

# Linear probing
"""
The systematic way of visiting each slot is a linear way of resolving collisions, in which we linearly look for the next
available slot by adding 1 to the previous hash value where we get the collision. This is known as linear probing. We can
resolve the conflict by adding 1 to the sum of the ordinal values of each character in the key string, which is further
used to compute the final hash value by taking its modulo according to the size of the hash table
"""

# Implementation using Linear probing
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable_linear:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        # ensure that the load factor of the hash table is always below the predefined maximum load factor
        self.MAXLOADFACTOR = 0.65 
        

    # Hash Function
    def _hash(self, key):
        mult = 1
        hv = 0

        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    # Metohd to insert in the hash table
    def put(self, key, value):
        # adding the key and the value to the HashItem class and then compute the hash value of the key.
        item = HashItem(key, value)
        h = self._hash(key)
        
        # obtaining the hash value of the key and if the slot is not empty
        while self.slots[h] != None:
            #the next free slot is checked by adding 1 to the previous hash value by applying the linear probing
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        # If the slot is empty, then increase the count by one and store the new element in the list at the required position. 
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    # Method to check f it is more than the set threshold
    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor > self.MAXLOADFACTOR:
            print("Load factor before growing the hash table", self.count / self.size )
            self.growth()
            print("Load factor after growing the hash table", self.count / self.size )


    # Method to grow the hash table
    def growth(self):
        # create a  new hash table double the size of the original hash table and then we initialize all of its slots to be None.
        New_Hash_Table = HashTable()
        New_Hash_Table.size = 2 * self.size
        New_Hash_Table.slots = [None for i in range(New_Hash_Table.size)]       

        for i in range(self.size):     
        #check all the filled slots in the original hash table where we have the data
            if self.slots[i] != None:
                #insert all these existing records into the new hash table,
                New_Hash_Table.put(self.slots[i].key, self.slots[i].value)
        # replace the size and slots of the existing table with the new hash table.
        self.size = New_Hash_Table.size
        self.slots = New_Hash_Table.slots


    # Method to retrieve elements 
    def get(self, key):
        # computed hash for the given key
        h = self._hash(key) 
        
        while self.slots[h] != None:
            #  If there is a match, we return the corresponding stored value.
            if self.slots[h].key == key:
                return self.slots[h].value
            # keep looking at the new hash value location com- puted as described
            h = (h+ 1) % self.size
        return None
    
    ## Implementing a hash table as a dictionary
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)


"""
# Test 1
ht = HashTable()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)
"""

"""
# Test 2
ht = HashTable()
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht[key]
    print(v)
print("The number of elements is: {}".format(ht.count))
"""


