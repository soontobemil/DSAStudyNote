class HashTable:
    def __init__(self, size):
        self.data = [None] * size  # Initialize the hash table with empty slots

    def hash_function(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def hash_set(self, key, value):
        address = self.hash_function(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key,value])
        return self.data

    def hash_get(self, key):
        address = self.hash_function(key)
        currentBucket = self.data[address]
        if (currentBucket):
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return False

    def hash_keys(self):
        if not len(self.data):
            return False
        else:
            hash_array = []
            for i in range(len(self.data)):
                if self.data[i]:  # Check if there's a bucket (list) at index i# Now it's safe to print the first element
                    hash_array.append(self.data[i][0][0])  # Append the key (the first element of the key-value pair)
                # self.data[i][0] is a key-value pair, and we want to append the key part (index 0)
        return hash_array

myHashTable = HashTable(50)
myHashTable.hash_set('apple', 10000)
myHashTable.hash_set('oranges', 54)
myHashTable.hash_keys()

print(myHashTable.hash_keys())
