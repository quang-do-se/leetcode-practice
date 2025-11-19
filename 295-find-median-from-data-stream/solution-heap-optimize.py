from heapq import heappushpop, heappush


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


sol = MedianFinder()
sol.addNum(4)
print(sol.findMedian())
sol.addNum(3)
print(sol.findMedian())
sol.addNum(2)
print(sol.findMedian())
sol.addNum(1)
print(sol.findMedian())
sol.addNum(5)
print(sol.findMedian())
print()

sol = MedianFinder()
sol.addNum(1)
print(sol.findMedian())
sol.addNum(2)
print(sol.findMedian())
sol.addNum(3)
print(sol.findMedian())
print()

sol = MedianFinder()
sol.addNum(40)
print(sol.findMedian())
sol.addNum(12)
print(sol.findMedian())
sol.addNum(16)
print(sol.findMedian())
sol.addNum(14)
print(sol.findMedian())
