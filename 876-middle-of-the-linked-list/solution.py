from typing import Optional
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow


sol = Solution()
print(sol.middleNode(LinkedList.generate_from_array([1,2,3,4,5,6])).val == 4)
print(sol.middleNode(LinkedList.generate_from_array([1,2,3,4,5])).val == 3)
print(sol.middleNode(LinkedList.generate_from_array([1,2,3,4])).val == 3)
print(sol.middleNode(LinkedList.generate_from_array([1,2])).val == 2)
print(sol.middleNode(LinkedList.generate_from_array([1])).val == 1)
print(sol.middleNode(LinkedList.generate_from_array([])) == None)
