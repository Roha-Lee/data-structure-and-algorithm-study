import hashlib

class HashTableChaining:
    def __init__(self, data, capacity=1000):
        self._capacity = capacity
        self.hash_table = [[] for _ in range(capacity)]
        self.insert(data)


    def __str__(self):
        return 'Hash Table\n' + str(self.hash_table).replace('],','],\n')
    

    def _hash(self, key):
        # return hash(key) % self._capacity
        hash_object = hashlib.sha256()
        hash_object.update(key.encode())
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16) % self._capacity


    def _check_and_insert(self, new_key, new_value):
        addr = self._hash(new_key)
        slot = self.hash_table[addr]
        for index, (key, _) in enumerate(slot):
            if key == new_key:
                slot[index] = (new_key, new_value)    
                return
        slot.append((new_key, new_value))


    def insert(self, data):
        for key, value in data:
            self._check_and_insert(key, value)
            

    def get_data(self, key):
        addr = self._hash(key)
        for curr_key, curr_value in self.hash_table[addr]:
            if curr_key == key:
                return curr_value 
        return 'Not Found!'


class HashTableLinearProbing:
    def __init__(self, data, capacity=1000):
        self._capacity = capacity
        self.hash_table = [None for _ in range(capacity)]
        self.insert(data)


    def __str__(self):
        return 'Hash Table\n' + str(self.hash_table).replace('None,','None,\n').replace('),','),\n')
    

    def _hash(self, key):
        # return hash(key) % self._capacity
        hash_object = hashlib.sha256()
        hash_object.update(key.encode())
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16) % self._capacity


    def _check_and_insert(self, new_key, new_value):
        addr = self._hash(new_key)
        if self.hash_table[addr]:
            if self.hash_table[addr][0] == new_key:
                self.hash_table[addr] = (new_key, new_value)
                return 
            for new_addr in list(range(addr+1, len(self.hash_table))) + list(range(0, addr)):
                
                if not self.hash_table[new_addr]:
                    self.hash_table[new_addr] = (new_key, new_value)
                    return
            print('Cannot insert key %s. Hash table is full.'%(new_key))
        else:
            self.hash_table[addr] = (new_key, new_value)


    def insert(self, data):
        for key, value in data:
            self._check_and_insert(key, value)
            

    def get_data(self, key):
        addr = self._hash(key)
        for new_addr in list(range(addr, len(self.hash_table))) + list(range(0, addr)):
            if not self.hash_table[new_addr]:
                return "Not Found."
            if self.hash_table[new_addr][0] == key:
                return self.hash_table[new_addr][1]
        return "Not Found."


if __name__ == '__main__':
    def hash_table_chaining_test():
        data = [('Yunhee', '01011112222'), 
                ('Jongil', '01022223333'),
                ('Jongho', '01033334444'),
                ('Inchan', '01044445555'),
                ('Minsu', '01055556666'),
                ('Seongbin', '01066667777')]

        hash_table = HashTableChaining(data, 15)
        print(hash_table)
        print(hash_table.get_data('Jongil'))    
        print(hash_table.get_data('Inchan'))    
        print(hash_table.get_data('Tan'))

        hash_table.insert([('Jongil', '00000000000'),
                           ('Yunsoo', '11111111111'),
                           ('Yongjae', '11111112222')])
        print(hash_table)


    def hash_table_linear_probing_test():
        data = [('Yunhee', '01011112222'), 
                ('Jongil', '01022223333'),
                ('Jongho', '01033334444'),
                ('Inchan', '01044445555'),
                ('Minsu', '01055556666'),
                ('Seongbin', '01066667777')]

        hash_table = HashTableLinearProbing(data, 7)
        print(hash_table)
        print(hash_table.get_data('Jongil'))    
        print(hash_table.get_data('Inchan'))    
        print(hash_table.get_data('Tan'))

        hash_table.insert([('Jongil', '00000000000'),
                           ('Yunsoo', '11111111111'),
                           ('Yongjae', '11111112222')])
        print(hash_table)



    hash_table_chaining_test()
    hash_table_linear_probing_test()