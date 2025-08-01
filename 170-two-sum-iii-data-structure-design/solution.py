class TwoSum:

    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        self.nums[number] = self.nums.get(number, 0) + 1
            
    def find(self, value: int) -> bool:
        for current in self.nums:
            opposite = value - current

            if opposite in self.nums:
                if current != opposite or self.nums[opposite] > 1:
                    return True 
                
        return False