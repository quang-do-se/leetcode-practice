import heapq


class MedianFinder:

    def __init__(self):
        self.left_heap = []  # max heap
        self.right_heap = []  # min heap
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1

        # Add the num to the right heap, pop out the smallest item in the right heap and add it back to the left heap
        heapq.heappush(self.right_heap, num)
        heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

        # Re-balance
        while len(self.left_heap) > len(self.right_heap):
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))

    def findMedian(self) -> float:
        if self.size == 0:
            raise Exception("No input")

        if self.size % 2 == 0:
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
