class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = dict()
        for i in range(len(nums)):
            k = target - nums[i]

            if k in seen:
                return [seen[k], i]

            seen[nums[i]] = i

        return []
    

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))
print(sol.twoSum([3,3], 6))