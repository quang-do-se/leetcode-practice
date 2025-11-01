from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)

    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Perform the QuickSelect algorithm on the list"""
        distances = [(self.squared_distance(point), point) for point in points]   # List of (distance, point)

        left, right = 0, len(distances) - 1
        pivot_index = len(distances)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = self.partition(distances, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1

        # Return the first k elements of the partially sorted list
        return [point for (_, point) in distances[:k]]

    def partition(self, distances: List[tuple], left: int, right: int) -> int:
        """Partition the list around the pivot value"""
        pivot_distance = self.choose_pivot(distances, left, right)[0]

        while left <= right:
            # Iterate through the range and swap elements to make sure
            # that all points closer than the pivot are to the left
            if distances[left][0] >= pivot_distance:
                distances[left], distances[right] = distances[right], distances[left]
                right -= 1
            else:
                left += 1

        return left

    def choose_pivot(self, distances: List[int], left: int, right: int) -> int:
        """Choose a pivot element of the list"""
        return distances[left + (right - left) // 2]

    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2


sol = Solution()
print(sol.kClosest([[1, 3], [-2, 2]], 1))
print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
