import random

class RandomizedSet:

    def __init__(self):
        self.num_to_index = {}
        self.index_to_num = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        if val not in self.num_to_index:
            self.num_to_index[val] = self.count
            self.index_to_num[self.count] = val
            self.count += 1

            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.num_to_index:
            val_index = self.num_to_index[val]

            if val_index == self.count - 1: # deleting index is the last index
                self.index_to_num.pop(val_index)
            else: # swap the last element to the deleting index
                self.index_to_num[val_index] = self.index_to_num[self.count - 1]
                self.num_to_index[self.index_to_num[self.count - 1]] = val_index
                self.index_to_num.pop(self.count - 1)

            self.num_to_index.pop(val)
            self.count -= 1

            return True
        else:
            return False

    def getRandom(self) -> int:
        random_index = random.randint(0, self.count - 1)

        return self.index_to_num[random_index]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(3))
print(obj.insert(4))


print("Random:", obj.getRandom())
print("Random:", obj.getRandom())
print("Random:", obj.getRandom())
print("Random:", obj.getRandom())
print("Random:", obj.getRandom())
print("Random:", obj.getRandom())
print("Random:", obj.getRandom())
print("Random:", obj.getRandom())