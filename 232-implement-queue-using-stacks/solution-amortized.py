class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.s1_head = None

    def push(self, x: int) -> None:
        if not self.s1:
            self.s1_head = x 
        
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        
        return self.s1_head

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0


sol = MyQueue()
sol.push(1)
sol.push(2)
sol.push(3)
sol.pop()
sol.push(4)
print(sol.peek())