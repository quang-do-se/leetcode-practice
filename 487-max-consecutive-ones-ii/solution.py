from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_one_count = 0
        curr_one_count = 0
        zero_count = 0
        max_one_count = 0

        for e in nums:
            if e == 1:
                curr_one_count += 1
            else:
                if curr_one_count > 0:
                    expand_one_count = curr_one_count + 1
                    if zero_count == 1:
                        expand_one_count = expand_one_count + prev_one_count

                    max_one_count = max(expand_one_count, max_one_count)

                    prev_one_count = curr_one_count
                    curr_one_count = 0
                    zero_count = 1
                else:
                    zero_count += 1

        if zero_count == 0:
            return curr_one_count
        elif zero_count > 0:
            expand_one_count = curr_one_count + 1
            if zero_count == 1:
                expand_one_count = expand_one_count + prev_one_count

            max_one_count = max(expand_one_count, max_one_count)

        return max_one_count


sol = Solution()
print(sol.findMaxConsecutiveOnes([0, 1, 1, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 0]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 0, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 0, 1, 1]) == 6)
print(sol.findMaxConsecutiveOnes([1, 1, 1, 0, 0, 1, 1]) == 4)
print(sol.findMaxConsecutiveOnes([1, 1, 0, 0, 1, 1, 1, 1]) == 5)
print(sol.findMaxConsecutiveOnes([0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]) == 7)
print(sol.findMaxConsecutiveOnes([0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0]) == 7)