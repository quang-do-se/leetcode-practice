import heapq


class MedianFinder:

    def __init__(self):
        self.left_heap = []  # max heap
        self.right_heap = []  # min heap
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1

        if self.size <= 2:
            heapq.heappush(self.right_heap, num)

            if self.size == 2:
                top_right = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -top_right)
            return

        if self.right_heap and self.left_heap:
            if num >= self.right_heap[0]:
                heapq.heappush(self.right_heap, num)
            else:
                heapq.heappush(self.left_heap, -num)

        # Re-balance
        if len(self.right_heap) > len(self.left_heap):
            longer_heap = self.right_heap
            shorter_heap = self.left_heap
        else:
            longer_heap = self.left_heap
            shorter_heap = self.right_heap

        while len(longer_heap) > len(shorter_heap):
            print("Re-balance")
            top_longer = heapq.heappop(longer_heap)
            heapq.heappush(shorter_heap, -top_longer)

    def findMedian(self) -> float:
        if self.size == 0:
            raise Exception("No input")

        if self.size % 2 == 0:
            return (-self.left_heap[0] + self.right_heap[0]) / 2

        return (
            self.right_heap[0]
            if len(self.right_heap) > len(self.left_heap)
            else -self.left_heap[0]
        )


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
