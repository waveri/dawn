class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h]=(key,value)
        else:
            new_h=self.find_slot(key,h)
        print(self.arr)

    def __getitem__(self, key):
        h=self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range=self.get_prob_range(key)
        for prob_index in prob_range:
            element=self.arr[prob_index]
            if element is None:
                return
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h=self.get_hash(key)
        prob_range=self.get_prob_range(key)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                raise Exception("element is already void")
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
            print(self.arr)


    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

t1=HashTable()
print(t1.get_prob_range(4))