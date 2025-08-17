from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        self.helper(list1, list2, dummy)

        return dummy.next
    
    def helper(self, list1: Optional[ListNode], list2: Optional[ListNode], merged_list: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            merged_list.next = list1 if list1 else list2
            return merged_list

        if list1.val <= list2.val:
            new_node = list1
            list1 = list1.next
        elif list1.val > list2.val:
            new_node = list2
            list2 = list2.next
        
        merged_list.next = new_node

        self.helper(list1, list2, new_node)


sol = Solution()
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1,2,4]), LinkedList.generate_from_array([1,3,4]))) == [1, 1, 2, 3, 4, 4])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([2]), LinkedList.generate_from_array([1]))) == [1, 2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1]), LinkedList.generate_from_array([2]))) == [1, 2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([1]), LinkedList.generate_from_array([]))) == [1])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([]), LinkedList.generate_from_array([2]))) == [2])
print(LinkedList.list_to_array(sol.mergeTwoLists(LinkedList.generate_from_array([5]), LinkedList.generate_from_array([1,2,4]))) == [1, 2, 4, 5])