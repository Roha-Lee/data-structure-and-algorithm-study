class HashTable:
    def __init__(self, data, capacity=1000):
        self._capacity = capacity
        self.hash_table = [[] for _ in range(capacity)]
        self._insert(data)


    def __str__(self):
        return "Hash Table\n" + str(self.hash_table).replace('],','],\n')
    

    def _hash(self, key):
        # [think of ROHA] A good hash function makes it evenly distributed across the hash table.
        return hash(key) % self._capacity


    def _insert(self, data):
        for key, value in data:
            addr = self._hash(key)
            self.hash_table[addr].append((key, value))
        

    def get_data(self, data):
        addr = self._hash(data)
        for key, value in self.hash_table[addr]:
            if key == data:
                return value 
        return "Not Found!"


if __name__ == '__main__':
    def hash_test():
        data = [('Yunhee', '01011112222'), 
                ('Jongil', '01022223333'),
                ('Jongho', '01033334444'),
                ('Inchan', '01044445555'),
                ('Minsu', '01055556666'),
                ('Seongbin', '01066667777')]

        hash_table = HashTable(data, 6)
        print(hash_table)
        print(hash_table.get_data('Jongil'))    
        print(hash_table.get_data('Inchan'))    
        print(hash_table.get_data('Tan'))
    
    hash_test()