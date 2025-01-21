# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
pick = 0
range = 0

def guess(num: int) -> int:
    if pick < num:
        return -1
    elif pick > num:
        return 1

    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            # mid = (low + high) // 2  # Could be overflow if low and high are big enough
            mid = low + (high - low) // 2  # Avoid overflow == (2 * low + high - low) // 2
            response = guess(mid)

            if response > 0:    # target is higher than guess
                low = mid + 1
            elif response < 0:  # target is smaller than guess
                high = mid - 1
            else:               # target is equal to guess
                return mid


sol = Solution()


range, pick = 10, 6
print(sol.guessNumber(range) == 6)

range, pick = 1, 1
print(sol.guessNumber(range) == 1)

range, pick = 2, 1
print(sol.guessNumber(range) == 1)

range, pick = 2, 2
print(sol.guessNumber(range) == 2)