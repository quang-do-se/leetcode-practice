import random


class RandomizedSet:

    def __init__(self):
        self.num_to_index = {}
        self.list = []
        self.count = 0

    def insert(self, val: int) -> bool:
        if val not in self.num_to_index:
            self.num_to_index[val] = len(self.list)
            self.list.append(val)

            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.num_to_index:
            val_index = self.num_to_index[val]

            if val_index == len(self.list) - 1:
                self.list.pop()
            else:
                last_element = self.list.pop()
                self.list[val_index] = last_element
                self.num_to_index[last_element] = val_index

            self.num_to_index.pop(val)

            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)


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
