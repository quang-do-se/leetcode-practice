from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Editorial solution
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                is_left_slot_available = (i == 0) or (flowerbed[i - 1] == 0)
                is_right_slot_available = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if is_left_slot_available and is_right_slot_available:
                    flowerbed[i] = 1
                    n -= 1

                    if n <= 0:
                        return True
            i += 1

        return n <= 0


sol = Solution()
print(sol.canPlaceFlowers([0], 1) == True)
print(sol.canPlaceFlowers([0, 1], 1) == False)
print(sol.canPlaceFlowers([1, 0], 1) == False)
print(sol.canPlaceFlowers([0, 0, 1], 1) == True)
print(sol.canPlaceFlowers([1, 0, 0], 1) == True)
print(sol.canPlaceFlowers([1, 0, 0, 1], 1) == False)
print(sol.canPlaceFlowers([1, 1, 0, 0], 1) == True)
print(sol.canPlaceFlowers([0, 0, 1, 1], 1) == True)
print(sol.canPlaceFlowers([1, 0, 0, 1], 2) == False)
print(sol.canPlaceFlowers([1, 1, 0, 0], 2) == False)
print(sol.canPlaceFlowers([0, 0, 1, 1], 2) == False)
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True)
print(sol.canPlaceFlowers([0, 0, 0, 1, 1], 1) == True)
print(sol.canPlaceFlowers([1, 1, 0, 0, 0], 1) == True)
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True)
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False)

print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1) == True)
print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 2) == True)
print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 3) == False)

print(sol.canPlaceFlowers([0, 1, 0, 1, 0], 0) == True)