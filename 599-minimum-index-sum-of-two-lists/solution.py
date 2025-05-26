from math import inf
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = inf
        common_list = []

        dict1 = {}
        for i in range(len(list1)):
            if list[i] not in dict1:
                dict1[list1[i]] = i
        
        for i in range(len(list2)):
            # Escape early
            if i > min_sum:
                break

            if list2[i] in dict1:
                sum = i + dict1[list2[i]]
                if sum < min_sum:
                    common_list = [list2[i]]
                    min_sum = sum
                elif sum == min_sum:
                    common_list += [list2[i]]

        return common_list


sol = Solution()
print(sol.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]) == ["Shogun"])
print(sol.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]) == ["Shogun"])
print(sol.findRestaurant(["happy","sad","good"], ["sad","happy","good"]) == ["sad","happy"])
print(sol.findRestaurant(["Show","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]) == [])