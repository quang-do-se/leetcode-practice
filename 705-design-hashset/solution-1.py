class MyHashSet:

    def __init__(self):
        self.capacity = 769
        self.buckets = [[] for _ in range(self.capacity)]
 
    def get_hash(self, key: int) -> int:
        return key % self.capacity
    
    def get_bucket(self, key: int) -> int:
        hash_key = self.get_hash(key)
        return self.buckets[hash_key]
        
    def add(self, key: int) -> None:
        bucket = self.get_bucket(key)        

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.get_bucket(key)

        return key in bucket


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1) == True)
print(myHashSet.contains(3) == False)
myHashSet.add(2)
print(myHashSet.contains(2) == True)
myHashSet.remove(2)
print(myHashSet.contains(2) == False)