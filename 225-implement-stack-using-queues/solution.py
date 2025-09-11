from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.top_element = []

    def push(self, x: int) -> None:
        self.top_element = x

        if self.q2:
            self.q2.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        self.top_element = None
        
        if self.q1:
            while len(self.q1) > 1:
                self.top_element = self.q1.popleft()
                self.q2.append(self.top_element)

            return self.q1.popleft()

        if self.q2:
            while len(self.q2) > 1:
                self.top_element = self.q2.popleft()
                self.q1.append(self.top_element)

            return self.q2.popleft()

        return None

    def top(self) -> int:
        if self.empty():
            return None

        return self.top_element

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.top())
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.top())
