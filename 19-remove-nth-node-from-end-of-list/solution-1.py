import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        slow = fast = head
        for _ in range(n):
            fast = fast.next

        # We are removing the first node in the list
        if fast is None:
            res = head.next
            head.next = None
            return res

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        remove = slow.next
        slow.next = slow.next.next
        remove.next = None
        return head


sol = Solution()
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1,2,3,4,5]), 1)) == [1, 2, 3, 4])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1,2,3,4,5]), 2)) == [1, 2, 3, 5])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1,2,3,4,5]), 5)) == [2, 3, 4, 5])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1]), 1)) == [])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1, 2]), 1)) == [1])