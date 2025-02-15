import os
import sys
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utility"))

from list_node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        curr_a = headA
        curr_b = headB

        while curr_a != None:
            visited.add(curr_a)
            curr_a = curr_a.next

        while curr_b != None:
            if curr_b in visited:
                return curr_b
            curr_b = curr_b.next

        return None