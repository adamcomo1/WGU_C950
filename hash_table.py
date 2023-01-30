# Hash Map Class

class HashTable:

    # constructor for class with default initial capacity of 10
    # All buckets are initially assigned with an empty list
    def __init__(self, initial_capacity=10):
        # hash table initialized with empty buckets
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # function for inserting new item into the hash table
    def insert(self, key, item):
        # hash functions to determine which bucket the item will be placed in
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # updates the key if it already exists in the table
        for k in bucket_list:
            if k[0] == key:
                k[1] = item
                return True
        # if they key does not exist the item is inserted to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Function for searching for an item using the key in the hash table
    # Return the item if found. If not found, returns none.
    def search(self, key):
        # finds the bucket list where the key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # searches for the key in the identified bucket
        for k in bucket_list:
            if k[0] == key:
                return k[1]
            return None

    # function for deleting items from the hash table using the key

    def delete(self, key):
        # finds the bucket list where the item will be deleted
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # deletes the item form the found bucket list if it is found
        for k in bucket_list:
            if k[0] == key:
                bucket_list.remove([k[0], k[1]])

