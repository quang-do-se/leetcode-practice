class MyHashSet:

    def __init__(self):
        self.list = [0] * 1000000

    def add(self, key: int) -> None:
        self.list[key] = 1

    def remove(self, key: int) -> None:
        self.list[key] = 0

    def contains(self, key: int) -> bool:
        return self.list[key] == 1


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1) == True)
print(myHashSet.contains(3) == False)
myHashSet.add(2)
print(myHashSet.contains(2) == True)
myHashSet.remove(2)
print(myHashSet.contains(2) == False)
