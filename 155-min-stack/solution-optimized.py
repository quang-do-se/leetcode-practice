# Optimized for space
class MinStack:

    def __init__(self):
        self.storage = []
        self.min_at_index = []

    def push(self, val: int) -> None:
        self.storage.append(val)

        current_min = self.min_at_index[-1][0] if self.min_at_index else float("inf")
        if val < current_min:
            self.min_at_index.append((val, len(self.storage) - 1))

    def pop(self) -> None:
        if len(self.storage) - 1 == self.min_at_index[-1][1]:
            self.min_at_index.pop()

        self.storage.pop()

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return self.min_at_index[-1][0]


minStack = MinStack()
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())  # return -3
print(minStack.push(-3))
print(minStack.pop())
print(minStack.getMin())  # return -3
print(minStack.pop())
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2
