class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        max_slots = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0: # beginning
                    if i + 1 >= len(flowerbed) or flowerbed[i + 1] != 1:
                        max_slots += 1
                        i += 1  # skip next slot
                elif i == len(flowerbed) - 1: # end
                    if flowerbed[i - 1] != 1:
                        max_slots += 1
                elif flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                    max_slots += 1
                    i += 1  # skip next slot

            i += 1

        return n <= max_slots


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