class Logger:

    def __init__(self):
       self.memory = {} 

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.memory or timestamp - self.memory[message] >= 10:
            self.memory[message] = timestamp
            return True

        return False