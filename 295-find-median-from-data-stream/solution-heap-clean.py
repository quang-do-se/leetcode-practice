from heapq import heappushpop, heappush, heappop


class MedianFinder:

    def __init__(self):
        self.left_heap = []  # max heap
        self.right_heap = []  # min heap

    def addNum(self, num: int) -> None:
        # Add the num to the right heap, pop out the smallest item in the right heap and add it back to the left heap
        heappush(self.left_heap, -heappushpop(self.right_heap, num))

        # Re-balance
        while len(self.left_heap) > len(self.right_heap):
            heappush(self.right_heap, -heappop(self.left_heap))

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return self.right_heap[0]


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
