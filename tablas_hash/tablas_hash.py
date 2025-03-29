class Person:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return True
        return False


if __name__ == "__main__":
    directory = Person(10)

    directory.insert("Alice", "123-456-7890")
    directory.insert("Bob", "987-654-3210")
    directory.insert("Charlie", "555-555-5555")

    print("Alice's number:", directory.search("Alice"))
    print("Bob's number:", directory.search("Bob"))

    directory.delete("Alice")
    print("Alice's number after deletion:", directory.search("Alice"))