class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.start = 0
        self.store = [None for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.store[(self.start + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.start = (self.start + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size > 0:
            return self.store[self.start]

        return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.store[(self.start + self.size - 1) % self.capacity]

        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1) == True)
print(myCircularQueue.enQueue(2) == True)
print(myCircularQueue.enQueue(3) == True)
print(myCircularQueue.enQueue(4) == False)
print(myCircularQueue.Front() == 1)
print(myCircularQueue.Rear() == 3)
print(myCircularQueue.isFull() == True)
print(myCircularQueue.deQueue() == True)
print(myCircularQueue.enQueue(4) == True)
print(myCircularQueue.Rear() == 4)