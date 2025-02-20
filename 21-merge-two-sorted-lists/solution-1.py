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

        sorted_list = ListNode(0)
        tail = sorted_list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return sorted_list.next


sol = Solution()
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1,2,4]), LinkedList.generate_from_array([1,3,4]))) == [1, 1, 2, 3, 4, 4])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([2]), LinkedList.generate_from_array([1]))) == [1, 2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1]), LinkedList.generate_from_array([2]))) == [1, 2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1]), LinkedList.generate_from_array([]))) == [1])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([]), LinkedList.generate_from_array([2]))) == [2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([5]), LinkedList.generate_from_array([1,2,4]))) == [1, 2, 4, 5])