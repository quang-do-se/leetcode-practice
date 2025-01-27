from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive approach
        return self.reverse_list_helper(None, head)

    def reverse_list_helper(self, reversed_list: Optional[ListNode], remaining_list: Optional[ListNode]) -> Optional[ListNode]:
        if remaining_list is None:
            return reversed_list

        node = remaining_list
        remaining_list = remaining_list.next

        node.next = reversed_list

        return self.reverse_list_helper(node, remaining_list)


sol = Solution()
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2,3,4,5]))) == [5,4,3,2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([1,2]))) == [2,1])
print(ListNode.list_to_array(sol.reverseList(ListNode.generate_from_array([]))) == [])