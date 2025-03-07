class Entry:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class MyHashMap:
    def __init__(self):
        self.capacity = 1069
        self.buckets = [[] for _ in range(self.capacity)]

    def get_hash(self, key: int) -> int:
        return key % self.capacity

    def get_bucket(self, key: int) -> int:
        hash_key = self.get_hash(key)
        return self.buckets[hash_key]

    def put(self, key: int, value: int) -> None:
        bucket = self.get_bucket(key)

        for item in bucket:
            if item.key == key:
                item.value = value
                return
        bucket.append(Entry(key, value))

    def get(self, key: int) -> int:
        bucket = self.get_bucket(key)

        for item in bucket:
            if item.key == key:
                return item.value
        return -1

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)

        for i in range(len(bucket)):
            if bucket[i].key == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
myHashMap = MyHashMap()
myHashMap.put(1, 1)   # The map is now [[1,1]]
myHashMap.put(2, 2)   # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))      # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))      # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 4)   # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))      # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2)   # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))      # return -1 (i.e., not found), The map is now [[1,1]]
myHashMap.remove(2)
myHashMap.remove(2)
myHashMap.remove(1)
myHashMap.remove(3)