from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                distance = i - map[nums[i]]
                if distance <= k:
                    return True

            map[nums[i]] = i

        return False

sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1], 3) == True)
print(sol.containsNearbyDuplicate([1,0,1,1], 1) == True)
print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False)