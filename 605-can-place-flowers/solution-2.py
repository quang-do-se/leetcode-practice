class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Optimized solution
        i = 0
        size = len(flowerbed)
        while i < size:
            if flowerbed[i] == 0:
                # If left slot is available and right slot is available
                if (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                    n -= 1
                    i += 1  # Skip next slot

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