import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode, LinkedList


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        i = 0
        fast = head
        while i < n and fast is not None:
            fast = fast.next
            i += 1

        prev = None
        curr = head
        while fast is not None:
            prev = curr
            curr = curr.next
            fast = fast.next

        if prev is not None:
            prev.next = curr.next
            curr.next = None
            return head
        else:
            res = head.next
            head.next = None
            return res


sol = Solution()
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1,2,3,4,5]), 1)) == [1, 2, 3, 4])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1,2,3,4,5]), 2)) == [1, 2, 3, 5])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1,2,3,4,5]), 5)) == [2, 3, 4, 5])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1]), 1)) == [])
print(LinkedList.list_to_array(sol.removeNthFromEnd(LinkedList.generate_from_array([1, 2]), 1)) == [1])