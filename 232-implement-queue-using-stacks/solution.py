class MyQueue:

    def __init__(self):
        self.stack = []
        self.mirror_stack = []
        self.head = None

    def push(self, x: int) -> None:
        if not self.head:
            self.head = x
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack) > 0:
            self.mirror_stack.append(self.stack.pop())

        if self.mirror_stack:
            removed_head = self.mirror_stack.pop()

        self.head = None
        while len(self.mirror_stack) > 0:
            if not self.head:
                self.head = self.mirror_stack.pop()
                self.stack.append(self.head)
            else:
                self.stack.append(self.mirror_stack.pop())

        return removed_head

    def peek(self) -> int:
        return self.head

    def empty(self) -> bool:
        return len(self.stack) == 0


sol = MyQueue()
sol.push(1)
sol.push(2)
sol.push(3)
sol.pop()
sol.pop()
print(sol.peek())
sol.pop()
print(sol.empty())
