import random

class RandomizedSet:
    
    def __init__(self):
        self.map = {}
        self.values = []
        self.index = -1  # to maintain the index of the inserted element in the map

    def getRandom(self):
        return random.choice(self.values) if self.values else None
    
    def insert(self, val):
        if self.map.get(val) is None:
            self.index += 1
            self.map[val] = self.index
            self.values.append(val)
            return True
        else:
            return False
    
    def remove(self, val):
        if self.map.get(val) is None:
            return False
        else:
            i = self.map[val]
            j = len(self.values) - 1

            # moving element at index i to the last index and then popping it from the values array
            temp = self.values[j]
            self.values[j] = self.values[i]
            self.values[i] = temp

            self.values.pop()  # pop the element from the values array : O(1)
            self.index -= 1  # reduce index by 1 every time
            self.map.pop(val)  # pop the element from the map too

            # "i != j" is important while removing the last element from the values array
            if len(self.values) > 0 and i != j:
                self.map[temp] = i

            return True


obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.insert(2)
param_3 = obj.remove(2)
param_4 = obj.remove(2)


["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
print(None, param_1, param_2, param_3, param_4)



