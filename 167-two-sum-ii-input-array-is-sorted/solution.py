from typing import List


class Solution:
    # Accepted solution but slow
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            search = target - numbers[i]

            low = i + 1
            high = len(numbers) - 1
            found = False
            
            while low <= high:
                mid = low + (high - low) // 2

                if search < numbers[mid]:
                    high = mid - 1                    
                elif search > numbers[mid]:
                    low = mid + 1
                else:
                    found = True
                    break
            
            if found:
                return [i + 1, mid + 1]
            
        return [-1, -1]


sol = Solution()
print(sol.twoSum([2,7,11,15], 9) == [1, 2])
print(sol.twoSum([2,3,4], 6) == [1, 3])
print(sol.twoSum([-1,0], -1) == [1, 2])