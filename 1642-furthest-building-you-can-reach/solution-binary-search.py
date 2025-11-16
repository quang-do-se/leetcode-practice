from typing import List


class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        # Make a sorted list of all the climbs needed to get to the given building.
        climbs = []
        for i in range(0, len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb > 0:
                # Each climb must have the index it reaches attached to it.
                climbs.append((climb, i + 1))
        climbs.sort()

        # Helper function to check whether or not the specified building is reachable
        # from the first building with the bricks and ladders we have.
        def is_reachable(building_index):
            # Check whether or not we have enough bricks and ladders to cover all
            # of these climbs. Bricks will be used before ladders.
            bricks_remaining = bricks
            ladders_remaining = ladders

            for climb, index in climbs:
                # If there are enough bricks left, use those.
                if index > building_index:
                    continue

                if climb <= bricks_remaining:
                    bricks_remaining -= climb
                # Otherwise, you'll have to use a ladder.
                elif ladders_remaining >= 1:
                    ladders_remaining -= 1
                # And if there are no ladders either, we can't reach buildingIndex.
                else:
                    return False
            return True

        # Do the binary search to find the final reachable building.
        lo = 0
        hi = len(heights) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if is_reachable(mid):
                lo = mid
            else:
                hi = mid - 1
        return hi  # Note that return lo would be equivalent.


sol = Solution()
print(sol.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4)
print(sol.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7)
print(sol.furthestBuilding([14, 3, 19, 3], 17, 0) == 3)
print(sol.furthestBuilding([1, 1, 6, 3, 11, 19, 25], 6, 2) == 5)
print(sol.furthestBuilding([1, 1, 6, 3, 11, 19, 25], 0, 0) == 1)
print(sol.furthestBuilding([7, 6, 5, 4, 3, 2, 1], 0, 0) == 6)
print(sol.furthestBuilding([1], 0, 0) == 0)
