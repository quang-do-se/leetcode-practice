class MinStack:

    def __init__(self):
        self.storage = []
        self.min_at_index = []
        self.size = 0

    def push(self, val: int) -> None:
        self.storage.append(val)
        current_min = self.min_at_index[-1] if self.min_at_index else float('inf')
        self.min_at_index.append(min(val, current_min))
        self.size += 1

    def pop(self) -> None:
        self.storage.pop()
        self.min_at_index.pop()
        self.size -= 1

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return self.min_at_index[-1]


minStack = MinStack();
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())  # return -3
print(minStack.pop())
print(minStack.top())     # return 0
print(minStack.getMin())  # return -2
print(minStack.pop())
print(minStack.pop())
