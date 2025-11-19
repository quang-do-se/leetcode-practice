import heapq

# Fastest
class MedianFinder:

    def __init__(self):
        self.left_heap = []  # max heap
        self.right_heap = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.right_heap or num >= self.right_heap[0]:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, -num)

        # Re-balance: right_heap's size is always +1 or equals to the left_heap's size
        if len(self.right_heap) > len(self.left_heap) + 1:
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
        elif len(self.left_heap) > len(self.right_heap):
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))

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
