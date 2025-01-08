class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Interesting solution
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

                if n <= 0:
                    return True

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