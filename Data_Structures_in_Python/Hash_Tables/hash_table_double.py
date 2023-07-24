###  Double hashing 

"""
In the double hashing collision resolution technique, we use two hashing functions. This technique works as follows.
Firstly, the primary hash function is used to compute the index position in the hash table, and whenever we get a collision,
we use another hash function to decide the next free slot to store the data by incrementing the hashing value


In order to find the next free slot in the hash table, we increment the hashing value, and this increment is fixed in the case
of linear probing and quadratic probing. Due to a fixed increment in the hashing value when we get collisions, the record is always
moved to the next available index position given by the hash function. It creates a continuous cluster of occupied index positions. 
This cluster grows whenever we get another record that has a hash value anywhere within the cluster.

However, in the case of the double hashing technique, the probing interval depends on the key data itself, meaning that we always map 
to the different index positions in the hash table whenever we get a collision, which, in turn, helps in avoiding the formation of clusters.
"""

class HashTable_double:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65
        self.prime_num = 5

    # Hash Function
    def _hash(self, key):
        mult = 1
        hv = 0
        
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size


    def put_double_hashing(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1

        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + j * (self.prime_num - (self._hash(key) % self.prime_num))) % self.size
            j = j+1
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    def get_double_hashing(self, key):
        h = self._hash(key)
        j = 1

        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + j * (self.prime_num - (self._hash(key) % self.prime_num))) % self.size
            j = j + 1
        return None


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
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)



"""
# Test 
ht = HashTable_double()
ht.put_double_hashing("good", "eggs")
ht.put_double_hashing("better", "spam")
ht.put_double_hashing("best", "cool")
ht.put_double_hashing("ad", "donot")
ht.put_double_hashing("ga", "collide")
ht.put_double_hashing("awd", "hello")
ht.put_double_hashing("addition", "ok")
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get_double_hashing(key)
    print(v)
print("The number of elements is: {}".format(ht.count))
"""
