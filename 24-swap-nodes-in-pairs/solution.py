import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        tail = self.swapPairs(head.next.next)

        new_head = head.next
        new_head.next = head
        head.next = tail

        return new_head


sol = Solution()

print(LinkedList.list_to_array(sol.swapPairs(LinkedList.generate_from_array([]))) == [])
print(LinkedList.list_to_array(sol.swapPairs(LinkedList.generate_from_array([1]))) == [1])
print(LinkedList.list_to_array(sol.swapPairs(LinkedList.generate_from_array([1, 2]))) == [2, 1])
print(LinkedList.list_to_array(sol.swapPairs(LinkedList.generate_from_array([1, 2, 3]))) == [2, 1, 3])
print(LinkedList.list_to_array(sol.swapPairs(LinkedList.generate_from_array([1, 2, 3, 4]))) == [2, 1, 4, 3])