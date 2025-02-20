from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        prev1 = None
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev1 = curr1
                curr1 = curr1.next
            else:
                next2 = curr2.next
                curr2.next = curr1

                if prev1 is None:
                    list1 = curr2
                else:
                    prev1.next = curr2

                prev1 = curr2
                curr2 = next2

        while curr2:
            prev1.next = curr2
            prev1 = curr2
            curr2 = curr2.next

        return list1


sol = Solution()
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1,2,4]), LinkedList.generate_from_array([1,3,4]))) == [1, 1, 2, 3, 4, 4])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([2]), LinkedList.generate_from_array([1]))) == [1, 2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1]), LinkedList.generate_from_array([2]))) == [1, 2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1]), LinkedList.generate_from_array([]))) == [1])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([]), LinkedList.generate_from_array([2]))) == [2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([5]), LinkedList.generate_from_array([1,2,4]))) == [1, 2, 4, 5])