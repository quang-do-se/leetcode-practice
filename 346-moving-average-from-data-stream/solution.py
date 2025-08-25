from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.capacity = size
        self.size = 0
        self.next_index = 0
        self.sum = 0
        self.store = [0 for _ in range(self.capacity)]

    def next(self, val: int) -> float:
        self.sum = self.sum + val - self.store[self.next_index]
        self.store[self.next_index] = val
        self.next_index = (self.next_index + 1) % self.capacity
        self.size = min(self.capacity, self.size + 1)
        
        return self.sum / self.size

movingAverage = MovingAverage(3)
print(movingAverage.next(1))
print(movingAverage.next(10))
print(movingAverage.next(3))
print(movingAverage.next(5))