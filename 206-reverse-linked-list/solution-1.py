from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Interative approach
        reversed_list = None

        while head is not None:
            next_head = head.next
            head.next = reversed_list
            reversed_list = head
            head = next_head

        return reversed_list


sol = Solution()
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2,3,4,5]))) == [5,4,3,2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2]))) == [2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([]))) == [])