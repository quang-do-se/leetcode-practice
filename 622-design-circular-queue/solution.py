class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.store = [None for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.start = 0
            self.end = 0
            self.store[self.start] = value
        else:
            self.end = (self.end + 1) % len(self.store)
            self.store[self.end] = value

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.start = (self.start + 1) % len(self.store)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size > 0:
            return self.store[self.start]

        return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.store[self.end]

        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.store)


myCircularQueue = MyCircularQueue(2)
print(myCircularQueue.enQueue(1)) # return True
print(myCircularQueue.enQueue(2)) # return True
print(myCircularQueue.enQueue(3)) # return True
print(myCircularQueue.enQueue(4)) # return False
print(myCircularQueue.Rear())     # return 3
print(myCircularQueue.isFull())   # return True
print(myCircularQueue.deQueue())  # return True
print(myCircularQueue.enQueue(4)) # return True
print(myCircularQueue.Rear())     # return 4