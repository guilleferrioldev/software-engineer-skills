# Quadratic probing

"""
This is also an open addressing scheme for resolving collisions in hash tables. It resolves the collision 
by computing the hash value of the key and adding successive values of a quadratic polynomial; the new hash 
is iteratively computed until an empty slot is found. If a collision occurs, the next free slots are checked 
at the locations h + 1², h + 2², h + 3², h + 4², and so on
"""

# Implementation using  quadratic probing
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable_quadratic:
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

    def get_quadratic(self, key):
        h = self._hash(key)
        j = 1
        
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h+ j*j) % self.size
            j = j + 1
        return None


    def put_quadratic(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1

        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + j*j) % self.size
            j = j+1
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

    
    ## Implementing a hash table as a dictionary
    def     __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)


"""
# Test 
ht = HashTable_quadratic()
ht.put_quadratic("good", "eggs")
ht.put_quadratic("ad", "packt")
ht.put_quadratic("ga", "books")
v = ht.get_quadratic("ga")
print(v)
"""
