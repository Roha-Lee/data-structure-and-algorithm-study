class HashTable:
    def __init__(self, data, capacity=1000):
        self._capacity = capacity
        self.hash_table = [[] for _ in range(capacity)]
        self.insert(data)


    def __str__(self):
        return 'Hash Table\n' + str(self.hash_table).replace('],','],\n')
    

    def _hash(self, key):
        # [ROHA's thought] A good hash function makes it evenly distributed across the hash table.
        return hash(key) % self._capacity


    def _check(self, slot, new_key):
        for key, _ in slot:
            if key == new_key:
                return False
        return True


    def insert(self, data):
        for key, value in data:
            addr = self._hash(key)
            if self._check(self.hash_table[addr], key):
                self.hash_table[addr].append((key, value))
            else:
                print('duplicated key [%s]'%(key))
    

    def get_data(self, data):
        addr = self._hash(data)
        for key, value in self.hash_table[addr]:
            if key == data:
                return value 
        return 'Not Found!'


if __name__ == '__main__':
    def hash_test():
        data = [('Yunhee', '01011112222'), 
                ('Jongil', '01022223333'),
                ('Jongho', '01033334444'),
                ('Inchan', '01044445555'),
                ('Minsu', '01055556666'),
                ('Seongbin', '01066667777')]

        hash_table = HashTable(data, 15)
        print(hash_table)
        print(hash_table.get_data('Jongil'))    
        print(hash_table.get_data('Inchan'))    
        print(hash_table.get_data('Tan'))

        hash_table.insert([('Jongil', '00000000000'),
                           ('Yunsoo', '11111111111'),
                           ('Yongjae', '11111112222')])
        print(hash_table)
    hash_test()